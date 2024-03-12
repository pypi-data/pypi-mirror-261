import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette
} from '@jupyterlab/apputils';

import {
  ToolbarButton
} from '@jupyterlab/apputils';

import {
  INotebookTracker
} from '@jupyterlab/notebook';

import {
  showDialog,
  Dialog
} from '@jupyterlab/apputils';

/**
 * Initialization data for the FIS_labextension extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'FIS_labextension:button',
  autoStart: true,
  requires: [ICommandPalette, INotebookTracker],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette, notebookTracker: INotebookTracker) => {
    console.log('JupyterLab extension FIS_labextension is activated!');

    // Create a command to execute when the button is clicked
    const command = 'FIS_labextension:button-clicked';
    app.commands.addCommand(command, {
      label: 'FIS_labextension Button',
      execute: async (args: any) => {
        console.log('FIS_labextension button clicked!');

        // Check if the required arguments are provided
        if (args.question && args.file) {
          // Use the provided question and file content for processing

          // Rest of the code remains unchanged
          // Get the current notebook
          const currentWidget = notebookTracker.currentWidget;

          // Check if a notebook is currently active
          if (currentWidget) {
            // Use type assertion to tell TypeScript that currentCell is of type Cell<ICellModel>
            const currentCell = currentWidget.content.activeCell as any;

            // Display a message in the cell while waiting for the response
            if (currentCell) {
              try {
                const requestBody = {
                  question: args.question,
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
                  const result = await showDialog({
                    title: 'API Response',
                    body: responseData,
                    buttons: [
                      Dialog.okButton({ label: 'Replace Cell' }),
                      Dialog.createButton({ label: 'Cancel' })
                    ]
                  });

                  // Handle the user's choice
                  if (result.button.accept) {
                    // Replace the cell content with the response
                    currentCell.model.value.text = responseData;

                    // Clear the cell output area if it exists
                    if (currentCell.outputArea) {
                      currentCell.outputArea.clear();
                    }
                  }
                  // Otherwise, do nothing (cancel operation)
                } else {
                  // Display an error message in the cell if the request fails
                  currentCell.outputArea.model.clear();
                  currentCell.outputArea.model.add({
                    output_type: 'stream',
                    name: 'stderr',
                    text: `Request failed with status ${response.status}\n`
                  });
                }
              } catch (error) {
                // Display an error message in the cell if an exception occurs
                currentCell.outputArea.model.clear();
                currentCell.outputArea.model.add({
                  output_type: 'stream',
                  name: 'stderr',
                  text: `Error: ${error}\n`
                });
              }
            }
          }
        } else {
          console.error('Invalid arguments. Please provide both question and file.');
        }
      }
    });

    // Create a toolbar button with text
    const button = new ToolbarButton({
      iconClass: 'jp-Icon jp-Icon-16 jp-MaterialIcon my-FIS-labextension-icon',
      onClick: () => {
        // Display an error if the command is used without arguments
        console.error('Usage: myextension "explain" code.py');
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

export default extension;

