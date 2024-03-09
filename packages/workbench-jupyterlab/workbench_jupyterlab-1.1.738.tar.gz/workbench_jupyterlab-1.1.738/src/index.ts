/*
 * index.ts
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */

import rstudioHome from '../images/posit-icon-fullcolor.svg';
import rstudioPanel from '../images/posit-icon-unstyled.svg';

import { RStudioWorkbenchWidget } from './widget';

import { Panel, Widget } from '@lumino/widgets';
import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ICommandPalette } from '@jupyterlab/apputils';
import { LabIcon } from '@jupyterlab/ui-components';
import { ServerConnection } from '@jupyterlab/services';
import { heartbeat, stopHeartbeat } from './disconnectMonitor';
import { setupDisconnectNotification } from './disconnectAlert';

let homeUrl: string = '/home';

const rstudioIcon = new LabIcon({
  name: 'workbench_jupyterlab:home-icon',
  svgstr: rstudioHome,
});

const rstudioPanelIcon = new LabIcon({
  name: 'workbench_jupyterlab:panel-icon',
  svgstr: rstudioPanel,
});

function returnHome(): void {
  location.assign(homeUrl);
}

function registerCommands(app: JupyterFrontEnd, palette: ICommandPalette): void {
  var regex = /(s\/[\w]{5}[\w]{8}[\w]{8}\/)/g;
  const settings = ServerConnection.makeSettings();
  homeUrl = settings.baseUrl.replace(regex, 'home/');

  // Register command to return to RStudio Workbench home
  const command = 'workbench_jupyterlab:return-home';
  app.commands.addCommand(command, {
    label: 'Return to Posit Workbench Home',
    caption: 'Return to Posit Workbench Home',
    execute: returnHome
  });
  palette.addItem({ command, category: 'Posit Workbench' });
}

function addRStudioIcon(app: JupyterFrontEnd): void {
  // Add RStudio icon that returns the user to home to menu bar
  const rstudio_widget = new Widget();
  rstudio_widget.id = 'rsw-icon';
  rstudio_widget.node.onclick = returnHome;

  rstudioIcon.element({
    container: rstudio_widget.node,
    justify: 'center',
    margin: '2px 5px 2px 5px',
    height: 'auto',
    width: '20px',
  });
  app.shell.add(rstudio_widget, 'top', { rank: 1 });
}

function addSideBar(app: JupyterFrontEnd): void{
  // Add the RSW side bar widget to the left panel
  const panel = new Panel();
  panel.id = 'RStudio-Workbench-tab';
  panel.title.icon = rstudioPanelIcon;
  panel.addWidget(new RStudioWorkbenchWidget());
  app.shell.add(panel, 'left', { rank: 501 });
}

function activate(app: JupyterFrontEnd, palette: ICommandPalette) {
  registerCommands(app, palette);
  addRStudioIcon(app);
  addSideBar(app);
  heartbeat(returnHome);
  setupDisconnectNotification();
}

function deactivate() {
  stopHeartbeat();
}

const plugin: JupyterFrontEndPlugin<void> = {
  // Initialization data for the workbench_jupyterlab extension.
  id: 'workbench-jupyterlab',
  autoStart: true,
  requires: [ ICommandPalette ],
  activate, 
  deactivate
};

export default plugin;
