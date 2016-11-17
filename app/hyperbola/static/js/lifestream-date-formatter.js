// minified and inlined in lifestream_base.html

/* exported HyperbolaDateFormatter */
var HyperbolaDateFormatter = (function() {
    "use strict";

    var formatDate = function(date) {
        var formatter = window.Intl.DateTimeFormat(undefined, {
            day: "numeric",
            month: "short",
            year: "numeric",
            hour: "numeric",
            minute: "2-digit",
            timeZoneName: "short"
        });
        return formatter.format(date);
    };

    var localizeDate = function() {}; // noop
    if (window.Intl && typeof window.Intl === "object") {
        localizeDate = function(timestamp, selector) {
            var d = new Date();
            d.setTime(timestamp * 1000);
            document.getElementById(selector).innerText = formatDate(d);
        };
    }

    return {
        "localize": localizeDate
    };
})();

window["HyperbolaDateFormatter"] = HyperbolaDateFormatter;
