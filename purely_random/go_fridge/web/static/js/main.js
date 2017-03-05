function autoRefresh(element) {
  element.src = element.src.split('?')[0] + '?' + new Date().getTime();
  setTimeout(_.partial(autoRefresh, element), 5000); // refresh every 50ms
}

$(function() {
  //autoRefresh($('#fridge-img')[0]);
});

// Quantcast tag
var _qevents = _qevents || [];

(function() {
var elem = document.createElement('script');
elem.src = (document.location.protocol == "https:" ? "https://secure" : "http://edge") + ".quantserve.com/quant.js";
elem.async = true;
elem.type = "text/javascript";
var scpt = document.getElementsByTagName('script')[0];
scpt.parentNode.insertBefore(elem, scpt);
})();

_qevents.push(
{qacct:"p-f9m9BCQpHNAQ2",labels:""}
);
