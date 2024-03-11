"use strict";
(self["webpackChunkFIS_extension"] = self["webpackChunkFIS_extension"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);




/**
 * Initialization data for the FIS_labextension extension.
 */
const extension = {
    id: 'FIS_labextension:button',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker],
    activate: (app, palette, notebookTracker) => {
        console.log('JupyterLab extension FIS_labextension is activated!');
        // Create a command to execute when the button is clicked
        const command = 'FIS_labextension:button-clicked';
        app.commands.addCommand(command, {
            label: 'FIS_labextension Button',
            execute: async () => {
                console.log('FIS_labextension button clicked!');
                // Get the current notebook
                const currentWidget = notebookTracker.currentWidget;
                // Check if a notebook is currently active
                if (currentWidget) {
                    // Use type assertion to tell TypeScript that currentCell is of type Cell<ICellModel>
                    const currentCell = currentWidget.content.activeCell;
                    // Display a message in the cell while waiting for the response
                    if (currentCell) {
                        try {
                            const requestBody = {
                                question: currentCell.model.toJSON().source,
                                prompt: ''
                            };
                            // Make an HTTP request to your endpoint
                            const response = await fetch('http://127.0.0.1:5001/endpoint', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                    // Add any other headers if needed
                                },
                                body: JSON.stringify(requestBody)
                            });
                            // Check if the request was successful (status code 200)
                            if (response.ok) {
                                // Parse the response
                                const responseData = await response.text();
                                // Show a dialog with options
                                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
                                    title: 'API Response',
                                    body: responseData,
                                    buttons: [
                                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: 'Replace Cell' }),
                                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.createButton({ label: 'Cancel' })
                                    ]
                                });
                                // Handle the user's choice
                                if (result.button.accept) {
                                    // Replace the cell content with the response
                                    currentCell.model.value.text = responseData;
                                    // Check if the cell has an output area
                                    if (currentCell.outputArea) {
                                        // Clear the cell output area if it exists
                                        currentCell.outputArea.model.clear();
                                    }
                                }
                                // Otherwise, do nothing (cancel operation)
                            }
                            else {
                                // Display an error message in the cell if the request fails
                                if (currentCell.outputArea) {
                                    currentCell.outputArea.model.clear();
                                    currentCell.outputArea.model.add({
                                        output_type: 'stream',
                                        name: 'stderr',
                                        text: `Request failed with status ${response.status}\n`
                                    });
                                }
                            }
                        }
                        catch (error) {
                            // Display an error message in the cell if an exception occurs
                            if (currentCell.outputArea) {
                                currentCell.outputArea.model.clear();
                                currentCell.outputArea.model.add({
                                    output_type: 'stream',
                                    name: 'stderr',
                                    text: `Error: ${error}\n`
                                });
                            }
                        }
                    }
                }
            }
        });
        // Create a toolbar button with text
        const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
            iconClass: 'jp-Icon jp-Icon-16 jp-MaterialIcon my-FIS-labextension-icon',
            onClick: () => {
                app.commands.execute(command);
            },
            tooltip: 'FIS_labextension Button',
            label: 'FIS_LabExtension'
        });
        // Add the button to the notebook toolbar when a notebook is activated
        notebookTracker.widgetAdded.connect((sender, nbPanel) => {
            nbPanel.toolbar.insertItem(11, 'FIS_labextension:button-clicked', button);
        });
        // Add the button to the command palette
        palette.addItem({ command, category: 'FIS_labextension' });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.c1b9e2d8410195807bff.js.map