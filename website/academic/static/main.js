// Search bar related UI events
(function() {

	// Select elements
	var wrapper = document.getElementById("search-wrapper");
	var input = document.getElementById("search-input");
	var clear = document.getElementById("search-clear");

	// Callbacks
	var triggerResultLayout = function() {
		if (document.body.dataset.layout != "result")
			document.body.dataset.layout = "result";
	};
	var focusSearchBar = function() {
		wrapper.dataset.focus = "true";
	};
	var blurSearchBar = function() {
		wrapper.dataset.focus = "false";
	};
	var clearInputBox = function(event) {
		event.preventDefault();
		input.value = "";
	};
	var clearBackForwardCache = function(event) {
		if (event.persisted && input.dataset.original)
			input.value = input.dataset.original;
	};

	// Bind listeners
	input.addEventListener("input", triggerResultLayout);
	input.addEventListener("click", triggerResultLayout);
	input.addEventListener("focus", focusSearchBar);
	input.addEventListener("blur", blurSearchBar);
	clear.addEventListener("click", clearInputBox);
	clear.addEventListener("mousedown", clearInputBox);
	window.addEventListener("pageshow", clearBackForwardCache);

	// Auto focus if the page is originated in home layout
	if (document.body.dataset.layout == "home" && !window.browser.ie)
		input.focus();
})();