// minified and inlined in lifestream_base.html

var HyperbolaDateFormatter = (function() {
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
        var p = "0" + n;
        return p.substring(p.length-2);
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
    }
})();
