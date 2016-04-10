// minified and inlined in lifestream_base.html

/* exported HyperbolaDateFormatter */
var HyperbolaDateFormatter = (function() {
    "use strict";

    var months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec"
    ];

    var pad = function(n) {
        return ("0" + n).slice(-2);
    };

    var formatDate = function(date) {
        return pad(date.getHours()) + ":" + pad(date.getMinutes()) +
            " " + months[date.getMonth()] + " " + pad(date.getDate()) +
            " " + date.getFullYear();
    };

    return {
        write: function(timestamp) {
            var d = new Date();
            d.setTime(timestamp * 1000);
            document.write(formatDate(d));
        }
    };
})();
