var div = document.getElementById('content_div');

function modeChanged()
{
    gadgets.window.adjustHeight();
}

function init()
{
    if (wave && wave.isInWaveContainer()) {
        wave.setModeCallback(modeChanged);
    }
    gadgets.window.adjustHeight();
}
gadgets.util.registerOnLoadHandler(init);
