var idoc = app.activeDocument;
var abs = idoc.artboards;

for (var a=abs.length-1; a>=0; a--) {
    idoc.selection = null;
    thisBoard = abs[a];

    // activate each artboard
    idoc.artboards.setActiveArtboardIndex (a);

    // select all in artboard
    idoc.selectObjectsOnActiveArtboard();

    if(!idoc.selection.length) {
        // delete artboard if it is empty,
        thisBoard.remove();
    } else {
        // fit artboard to selection
        idoc.fitArtboardToSelectedArt(a);
    }
}

idoc.selection = null;