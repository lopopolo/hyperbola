// minified and inlined in lifestream_base.html

(function(exports) {
    "use strict";

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

    exports["HyperbolaDateFormatter"] = {
        "localize": localizeDate
    };
})(window);
