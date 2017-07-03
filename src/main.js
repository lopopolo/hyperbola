"use strict";

require("hyperbola.browser");

var localizeDate = function() {}; // noop
if (exports.Intl && typeof exports.Intl === "object") {
    var formatter = new exports.Intl.DateTimeFormat(undefined, {
        day: "numeric",
        month: "short",
        year: "numeric",
        hour: "numeric",
        minute: "2-digit",
        timeZoneName: "short"
    });
    localizeDate = function(timestamp, selector) {
        var d = new Date();
        d.setTime(timestamp * 1000);
        document.getElementById(selector).innerText = formatter.format(d);
    };
}

module.exports = {
    HyperbolaDateFormatter: localizeDate,
    retinajs: require("retinajs/dist/retina.js"),
};
