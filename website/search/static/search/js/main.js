"use strict";

// Naive browser detection
(function() {
	window.browser = {
		ie: /Trident|MSIE/i.test(navigator.userAgent),
		firefox: /Firefox/i.test(navigator.userAgent)
	};
})();

// XHR helpers
(function() {

	// Get HTML chunks
	window.getChunk = function(uri, callback) {

		// Create XMLHttpRequest object
		var xhr = null;
		if (window.XMLHttpRequest)
			xhr = new window.XMLHttpRequest();
		else if (window.ActiveXObject)
			xhr = new window.ActiveXObject("Microsoft.XMLHTTP");

		// XHR is not available
		if (!xhr)
			return callback(new Error("XHR is not available"), null);

		// Handle error
		xhr.onerror = function() {
			return callback(new Error("Network error"), null);
		};

		// Request aborted
		xhr.onabort = function() {
			return callback(new Error("Request aborted"), null);
		};

		// Successfully loaded
		xhr.onload = function() {

			// Check status code
			if (xhr.status === 200 || xhr.status === 304)
				return callback(null, xhr.responseText);

			// Invalid status code
			return callback(new Error(xhr.statusText), null);
		};

		// Fire the get request
		xhr.open("GET", uri, true);
		xhr.send(null);
	};
})();

// Transition tweening
(function() {

	// Simple requestAnimationFrame polyfill
	var raf = (function() {

		// Fallback to setTimeout @ 60Hz
		var fn = window.requestAnimationFrame;
		if (typeof(fn) != "function") {
			fn = function(callback) {
				setTimeout(callback, 17);
			};
		}

		// Fix skip frames in Firefox Quantum
		if (window.browser.firefox === true) {
			return function(callback) {
				fn(function() {
					fn(callback);
				});
			};
		}

		return fn;
	})();

	// Get computed transition duration
	var duration = function(node) {
		var raw = window.getComputedStyle(node).transitionDuration || "";
		return (parseFloat(raw) || 0) * (raw.indexOf("ms") > 0 ? 1 : 1000);
	};

	// Common pre-process step
	var pre = function(node, type, state, instant) {

		// Unmodified or forced to change immediately
		if (instant === true || node.dataset[type] == state) {
			node.dataset[type] = state;
			return false;
		}

		return true;
	};

	// Common post-process step
	var post = function(node, callback) {

		// Only callback once
		var guard = false;

		// Cancel the pending timer
		clearTimeout(node._transitionTimer);

		// Callback wrapper
		var done = function() {

			// Clear timeout
			clearTimeout(node._transitionTimer);

			// Already fired
			if (guard === true)
				return;

			// Clear the style property after transition
			node.style.cssText = "";

			// Update flag and callback
			guard = true;
			callback();
		};

		// Listen to the transitionend event if available
		node.addEventListener("transitionend", done);

		// Fallback to the plain old setTimeout with a sufficient timeout
		node._transitionTimer = setTimeout(done, duration(node) + 10);
	};

	// Optional callback
	var complete = function(node, callback) {
		if (typeof(callback) == "function")
			callback(node);
	};

	// Fading transition
	var fade = function(state, instant, callback) {

		// Pre-process
		var node = this;
		if (!pre(node, "fade", state, instant))
			return;

		// Ensure the element is rendered as block during the transition
		node.style.display = "block";

		// Update state
		raf(function() {
			node.dataset.fade = state;
			post(node, function() {
				complete(node, callback || instant);
			});
		});
	};

	// Collapsing transition
	var collapse = function(state, instant, callback) {

		// Pre-process
		var node = this;
		if (!pre(node, "collapse", state, instant))
			return;

		// Ensure the element is rendered as block during the transition
		node.style.display = "block";

		// From explicit height to target height
		node.style.maxHeight = state == "collapsed" ? (node.scrollHeight + "px") : "0px";
		raf(function() {
			node.style.maxHeight = state == "collapsed" ? "0px" : (node.scrollHeight + "px");
			node.dataset.collapse = state;
			post(node, function() {
				complete(node, callback || instant);
			});
		});
	};

	// Height clipping
	var clip = function(state, instant, callback) {

		// Pre-process
		var node = this;
		if (!pre(node, "clip", state, instant))
			return;

		// Get current height
		var prev = node.dataset.clip;
		var from = node.scrollHeight + "px";

		// Get target height
		node.dataset.clip = state;
		var to = node.scrollHeight + "px";

		// Show all inner elements during the transition
		node.dataset.clip = "false";
		node.style.maxHeight = from;
		raf(function() {
			node.style.maxHeight = to;
			post(node, function() {
				node.dataset.clip = state;
				complete(node, callback || instant);
			});
		});

	};

	// Export the binding function
	window.tween = function(node) {
		node.fade = fade.bind(node);
		node.collapse = collapse.bind(node);
		node.clip = clip.bind(node);
		return node;
	};
})();

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

// Censorship
(function() {

	// Censor class
	var Censor = function(profiles) {
		this.enabled = profiles.length > 0;
		this.profiles = Object.create(null);
		for (var i = 0; i < profiles.length; i++)
			this.profiles[profiles[i].name] = profiles[i];
	};

	Censor.prototype._createWarning = function() {

		// Already created
		if (document.getElementById("censored"))
			return false;

		// Create element
		var warn = document.createElement("div");
		warn.setAttribute("id", "censored");
		warn.classList.add("tips");
		warn.textContent = i18n.censorWarning;

		// Prepend to the result container
		var parent = document.querySelector("main");
		parent.insertBefore(warn, parent.firstChild);

		return true;
	};

	Censor.prototype._remove = function(node, depth) {

		// Invalid node
		var parent = node.parentNode;
		if (!node || !parent)
			return false;

		// Remove recursively
		node.parentNode.removeChild(node);
		if (depth > 0)
			return this._remove(parent, depth - 1);

		return true;
	};

	Censor.prototype._testAgainst = function(text, regexes) {
		for (var i = 0; i < regexes.length; i++)
			if (regexes[i].test(text))
				return true;
		return false;
	};

	Censor.prototype._getText = function(node, selector, attr) {

		// Get text from attribute
		if (typeof(attr) == "string")
			return node.getAttribute(attr);

		// Get text from child selector
		var contents = node.querySelectorAll(selector);
		var texts = [];
		for (var i = 0; i < contents.length; i++)
			texts.push(contents[i].textContent);

		return texts.join(" ");
	};

	Censor.prototype.filter = function(name, dry) {

		// Check availability
		if (!this.enabled || !this.profiles[name])
			return false;

		// Select candidate nodes
		var profile = this.profiles[name];
		var candidates = document.querySelectorAll(profile.nodeSelector);
		if (candidates.length === 0)
			return false;

		// Check each node
		var hit = false;
		for (var i = 0; i < candidates.length; i++) {
			var candidate = candidates[i];

			// Test regexes
			var text = this._getText(candidate, profile.contentSelector, profile.contentAttribute);
			if (!this._testAgainst(text, profile.regexes))
				continue;

			// We got a hit!
			hit = true;

			// Dry run
			if (dry === true)
				return true;

			// Remove by selector
			if (typeof(profile.removeSelector) == "string") {
				var removes = document.querySelectorAll(profile.removeSelector);
				for (var j = 0; j < removes.length; j++)
					this._remove(removes[j], 0);
			}

			// Remove self and parents
			if (typeof(profile.removeParents) == "number")
				this._remove(candidate, profile.removeParents);
		}

		// Jobs done
		if (!hit || dry === true)
			return hit;

		// Optional warning label
		if (profile.warning === true)
			this._createWarning();

		// Optional cleanup
		if (typeof(profile.cleanup) == "function")
			profile.cleanup();

		return hit;
	};

	// Simple cipher
	var cipher = function(x) {
		var r = [];
		var c = [];
		if (typeof(x) != "string" || x.length === 0)
			return r;
		x = window.atob(x).split("-");
		for (var i = 0; i < x.length; i++)
			c.push(String.fromCharCode(parseInt(x[i], 16)));
		c = c.join("").split("\n");
		for (var i = 0; i < c.length; i++)
			r.push(new RegExp(c[i], "i"));
		return r;
	};

	// Filter profiles
	var profiles = [];
	var l1 = cipher(window.i18n.censorLevel1);
	var l2 = cipher(window.i18n.censorLevel2).concat(l1);
	if (l1.length > 0) {
		profiles.push({
			name: "query",
			nodeSelector: "#search-input",
			contentAttribute: "data-original",
			removeSelector: "main>*",
			warning: true,
			regexes: l1
		});
		profiles.push({
			name: "web",
			nodeSelector: ".card[data-type=web]",
			contentSelector: "h3,p",
			removeParents: 0,
			warning: true,
			regexes: l1
		});
	}
	if (l2.length > 0) {
		profiles.push({
			name: "showcase",
			nodeSelector: "#showcase li",
			contentSelector: "h5,div>a",
			removeParents: 0,
			warning: false,
			regexes: l2
		});
		profiles.push({
			name: "card",
			nodeSelector: ".card[data-type=fact]",
			contentSelector: "header>div>h2,header>div>span",
			removeParents: 0,
			warning: true,
			regexes: l2
		});
		profiles.push({
			name: "fact",
			nodeSelector: ".fact",
			contentSelector: "dd",
			removeParents: 1,
			warning: true,
			regexes: l2,
			cleanup: function() {

				// Remove empty fact sections
				var sections = document.querySelectorAll(".card[data-type=fact]>div>section");
				for (var i = 0; i < sections.length; i++)
					if (sections[i].children[1].children.length === 0)
						sections[i].parentNode.removeChild(sections[i]);

				// Remove empty fact cards
				var cards = document.querySelectorAll(".card[data-type=fact]");
				for (var i = 0; i < cards.length; i++)
					if (cards[i].children[1].children.length === 0)
						cards[i].parentNode.removeChild(cards[i]);
			}
		});
	}

	// Create censor instance
	window.censor = new Censor(profiles);
	if (window.localStorage && window.localStorage.getItem("konami") == "30")
		window.censor.enabled = false;

	// First run
	window.censor.filter("query");
	window.censor.filter("card");
	window.censor.filter("fact");
	window.censor.filter("web");
})();

// Next page
(function() {

	// Select the next page button
	var getNextPageButton = function() {
		return document.querySelector(".card[data-type=next]");
	};

	// Load and render the next page
	var loadNextPage = function() {

		// Check the existence of the button
		var button = getNextPageButton();
		if (!button) return;

		// Enter loading state
		loadingNextPageButton();

		// Build the request URI
		var uri = "/search?ajax=1";
		uri += "&offset=" + button.dataset.offset;
		uri += "&size=" + button.dataset.size;
		uri += "&q=" + encodeURIComponent(button.dataset.input);

		// Get the next page
		window.getChunk(uri, function(err, content) {

			// Network error
			if (err) {
				resetNextPageButton();
				return console.error(err);
			}

			// Remove the stale button and append the new fragment
			var fragment = document.createRange().createContextualFragment(content);
			button.parentNode.replaceChild(fragment, button);

			// Censor new results
			if (window.censor)
				window.censor.filter("web");

			// Initialize the new button
			resetNextPageButton();
		});
	};

	// Reinitialize the next page button
	var resetNextPageButton = function() {

		// Check the existence of the button
		var button = getNextPageButton();
		if (!button) return;

		// Bind event listener and reset state
		button.addEventListener("click", loadNextPage);
		button.dataset.loading = "false";
		button.textContent = i18n.nextPageLoad;
	};

	// Enter the loading state
	var loadingNextPageButton = function() {

		// Check the existence of the button
		var button = getNextPageButton();
		if (!button) return;

		// Remove event listener and reset state
		button.removeEventListener("click", loadNextPage);
		button.dataset.loading = "true";
		button.textContent = i18n.nextPageLoading;
	};

	// Initialize the button
	resetNextPageButton();
})();

// Fact search result collapsing
(function() {

	// Layout constants
	var mobile = window.screen.width <= 760;
	var k_EXPANDED_CARDS = mobile ? 2 : 2;
	var k_EXPANDED_FACTS_MIXED = mobile ? 15 : 20;
	var k_EXPANDED_FACTS_DESCRIPTION = mobile ? 4 : 6;
	var k_EXPANDED_FACTS_PROPERTY = mobile ? 6 : 10;
	var k_EXPANDED_FACTS_TAG = mobile ? 10 : 15;
	var k_EXPANDED_FACTS_SYNONYM = mobile ? 4 : 6;

	// Initialize card elements
	var initCard = function(card, index) {

		// Initialize sections
		var sections = card.querySelectorAll("section[data-scope]");
		for (var i = 0; i < sections.length; i++)
			initSection(sections[i], card, index);

		// Interactive elements
		var header = card.children[0];
		var content = card.children[1];
		var hint = header.getElementsByTagName("a")[0];

		// Bind transitions
		window.tween(content);
		window.tween(hint);

		// Folding state
		var expanded = true;
		if (index >= k_EXPANDED_CARDS)
			expanded = false;
		if (index > 0 && mobile && card.getBoundingClientRect().bottom >= window.innerHeight)
			expanded = false;
		if (index > 0 && !mobile && card.getBoundingClientRect().top >= window.innerHeight)
			expanded = false;
		if (index > 0 && card.dataset.subtype == "value")
			expanded = false;

		// Fold cards
		card.dataset.folded = expanded ? "false" : "true";
		content.collapse(expanded ? "expanded" : "collapsed", true);
		hint.fade(expanded ? "hidden" : "visible", true);

		// Handle clicks
		header.addEventListener("click", function() {
			if (card.dataset.folded == "true") {
				card.dataset.folded = "false";
				content.collapse("expanded");
				hint.fade("hidden");
			} else {
				card.dataset.folded = "true";
				content.collapse("collapsed");
				hint.fade("visible");
			}
		});
	};

	// Initialize section elements
	var initSection = function(section, card, index) {

		// Initialize facts
		var facts = section.querySelectorAll(".fact");
		for (var i = 0; i < facts.length; i++)
			initFact(facts[i], section, card, index);

		// Truncate long sections
		var content = section.getElementsByTagName("div")[0];
		var cells = content.children;
		var limit = k_EXPANDED_FACTS_MIXED;
		switch (section.dataset.scope) {
			case "description":
				limit = k_EXPANDED_FACTS_DESCRIPTION;
				break;
			case "property":
				limit = k_EXPANDED_FACTS_PROPERTY;
				break;
			case "tag":
				limit = k_EXPANDED_FACTS_TAG;
				break;
			case "synonym":
				limit = k_EXPANDED_FACTS_SYNONYM;
				break;
		}
		if (cells.length <= limit)
			return;

		// Hide extra cells
		section.dataset.truncate = "peek";
		for (var i = limit; i < cells.length; i++)
			cells[i].dataset.extra = "true";

		// Bind transitions
		window.tween(content).clip("true", true);

		// Handle clicks
		var footer = section.lastElementChild;
		footer.addEventListener("click", function() {
			if (section.dataset.truncate == "peek") {
				section.dataset.truncate = "all";
				content.clip("false");
			} else {
				section.dataset.truncate = "peek";
				content.clip("true");
			}
		});
	};

	// Initialize fact elements
	var initFact = function(fact, section, card, index) {

		// Interactive elements
		var header = fact.children[0];
		var contexts = fact.children[1];
		var cell = fact.parentNode;

		// Bind transitions
		window.tween(contexts);

		// Determine initial layout
		if (card.dataset.subtype == "value") {
			contexts.collapse("expanded", true);
			cell.dataset.span = "row";
			fact.dataset.render = "tuple";
		} else {
			contexts.collapse("collapsed", true);
			cell.dataset.span = "cell";
			fact.dataset.render = "cell";
		}

		// Handle clicks
		header.addEventListener("click", function() {
			if (contexts.dataset.collapse == "collapsed") {
				cell.dataset.span = "row";
				fact.dataset.render = "tuple";
				contexts.collapse("expanded");
			} else {
				contexts.collapse("collapsed", function() {
					cell.dataset.span = "cell";
					fact.dataset.render = "cell";
				});
			}
		});
	};

	// Get all fact cards
	var cards = document.querySelectorAll(".card[data-type=fact]");
	for (var i = 0; i < cards.length; i++)
		initCard(cards[i], i);
})();

// Showcase carousel
(function() {

	// Carousel loop
	var offset = 0;
	var next = function() {

		// Break if we're no longer in the home layout
		if (document.body.dataset.layout != "home")
			return;

		// Select the next record by offset
		var wrapper = document.getElementById("showcase");
		var list = wrapper.getElementsByTagName("ul")[0];
		var record = list.children[(offset++) % list.children.length];

		// Fade in and out
		record.fade("visible", function() {
			setTimeout(function() {
				record.fade("hidden", function() {
					setTimeout(next, 1000);
				});
			}, 9000);
		});
	};

	// Fetch and inject showcases
	var inject = function() {

		// Break if we're no longer in the home layout
		if (document.body.dataset.layout != "home")
			return;

		// Fetch showcase chunks
		window.getChunk("/showcase", function(err, content) {

			// Failed to get chunks
			if (err)
				return console.error(err);

			// Inject fragment to the home section
			var fragment = document.createRange().createContextualFragment(content);
			document.getElementById("home").appendChild(fragment);

			// Censor showcases
			if (window.censor)
				window.censor.filter("showcase");

			// The fragment might be empty
			var wrapper = document.getElementById("showcase");
			var list = wrapper.getElementsByTagName("ul")[0];
			if (list.children.length === 0)
				return;

			// Sort randomly leveraging appendChild's auto removal
			for (var i = list.children.length; i >= 0; i--)
				list.appendChild(list.children[(Math.random() * i) | 0]);

			// Bind transitions and initialize states
			for (var i = 0; i < list.children.length; i++)
				window.tween(list.children[i]).fade("hidden", true);

			// Start the carousel
			setTimeout(next, 2000);
		});
	};

	// Initial delay after loaded
	if (document.body.dataset.layout == "home")
		setTimeout(inject, 4000);
})();

// Search suggestions
(function() {

	// Select elements
	var input = document.getElementById("search-input");
	var dropdown = document.getElementById("search-suggestions");
	var form = document.getElementById("search-form");

	// Retrieve suggestions
	var cache = Object.create(null);
	var retrieveSuggestions = function(text, size, callback) {

		// Concat query uri and use it as the cache key
		var uri = "/suggest?size=" + size + "&q=" + encodeURIComponent(text);

		// From cache
		if (cache[uri])
			return callback(null, cache[uri], true);

		// From upstream
		window.getChunk(uri, function(err, data) {

			// Parse and update cache
			return callback(err, data ? (cache[uri] = JSON.parse(data)) : null, false);
		});
	};

	// Render suggestion card
	var renderSuggestionCard = function(text, before, minimum) {

		// Ignore empty query text
		if (text.trim().length === 0)
			return;

		// Get the top suggestions
		retrieveSuggestions(text, 9, function(err, suggestions, fromCache) {

			// Do not render empty cards or cards with few suggestions
			if (err || !suggestions || suggestions.length < minimum)
				return;

			// Create suggestion card
			var div = document.createElement("div");
			div.setAttribute("class", "card");
			div.dataset.type = "suggest";

			// Create suggestion grid
			var ul = document.createElement("ul");
			ul.setAttribute("class", "queue-in");

			// Render links
			suggestions.forEach(function(content) {
				var li = document.createElement("li");
				var a = document.createElement("a");
				a.textContent = content;
				a.dataset.decoration = "search";
				a.setAttribute("href", "/search?q=" + encodeURIComponent(content));
				a.setAttribute("target", "_self");
				li.appendChild(a);
				ul.appendChild(li);
			});

			// Insert before the reference node
			div.appendChild(ul);
			document.querySelector("main").insertBefore(div, before || null);
		});
	};

	// Dropdown status flags
	var selected = 0;
	var original = "";

	// Clear the dropdown
	var clearDropdown = function() {
		selected = -1;
		while (dropdown.lastChild)
			dropdown.removeChild(dropdown.lastChild);
	};

	// Reset the active suggestion item
	var resetActiveItem = function() {
		for (var i = 0, l = dropdown.children.length; i < l; i++)
			dropdown.children[i].dataset.active = i === selected ? "true" : "false";
	};

	// Get index of a suggestion item
	var indexInDropdown = function(li) {
		for (var i = 0, l = dropdown.children.length; i < l; i++)
			if (dropdown.children[i] === li)
				return i;
		return -1;
	};

	// Mouse entering a suggestion item
	var enterDropdownItem = function() {
		selected = indexInDropdown(this);
		resetActiveItem();
	};

	// Mouse leaving an active item
	var leaveDropdownItem = function() {
		if (selected === indexInDropdown(this)) {
			selected = -1;
			resetActiveItem();
		}
	};

	// Update search box and submit
	var clickDropdownItem = function() {
		input.value = this.textContent;
		form.submit();
	};

	// Update the search dropdown
	var latest = 0;
	var updateDropdown = function(text) {

		// Get text from the search bar
		if (typeof(text) != "string") {
			var q = input.value;
			text = q.trim();

			// Preserve trailing spaces
			if (text.length > 0 && q[q.length - 1] == " ")
				text += " ";
		}

		// Clear the dropdown on empty strings
		if (text.length === 0)
			return clearDropdown();

		// Get top suggestions
		var id = ++latest % 0xFFFF;
		retrieveSuggestions(text, 8, function(err, suggestions, fromCache) {

			// Error or stale request ID
			if (err || id !== latest)
				return;

			// Build the dropdown
			var fragment = document.createDocumentFragment();
			suggestions.forEach(function(content) {
				var li = document.createElement("li");
				li.textContent = content;
				li.addEventListener("mouseenter", enterDropdownItem);
				li.addEventListener("mouseleave", leaveDropdownItem);
				li.addEventListener("mousedown", clickDropdownItem);
				fragment.appendChild(li);
			});

			clearDropdown();
			dropdown.appendChild(fragment);
		});
	};

	// Update the search dropdown on input
	var timeout = null;
	input.addEventListener("input", function() {
		original = input.value;
		clearTimeout(timeout);
		timeout = setTimeout(updateDropdown, 200);
	});

	// Update the search dropdown on focus
	input.addEventListener("focus", function() {
		original = input.value;
		clearDropdown();
		updateDropdown();
	});

	// Handle arrow keys and tab
	input.addEventListener("keydown", function(event) {

		// Do nothing on empty dropdowns
		var total = dropdown.children.length;
		if (total === 0)
			return;

		// Handle by key codes
		switch (event.keyCode) {
			case 9:
				event.preventDefault();
				if (total > 0) {
					original = input.value = dropdown.children[selected >= 0 ? selected : 0].textContent;
					updateDropdown();
				}
				break;
			case 38:
				event.preventDefault();
				selected = selected < 0 ? total - 1 : selected - 1;
				input.value = selected < 0 ? original : dropdown.children[selected].textContent;
				resetActiveItem();
				break;
			case 40:
				event.preventDefault();
				selected = selected + 1 >= total ? -1 : selected + 1;
				input.value = selected < 0 ? original : dropdown.children[selected].textContent;
				resetActiveItem();
				break;
		}
	});

	// Render suggestion card
	if (input.dataset.original && (!window.censor || !window.censor.filter("query", true))) {
		var button = document.querySelector("div.card[data-type=next]");
		renderSuggestionCard(input.dataset.original, button, button ? 6 : 1);
	}
})();

// Bibliography
(function() {

	// Get the right column
	var right = document.getElementById("right");

	// Collect top sources from facts
	var collect = function(count) {

		// Initialize candidate collector
		var candidates = Object.create(null);

		// Add to collector
		var add = function(card, section, fact, context, source, i, j, k, m, n) {

			// Confidence level
			var dl = fact.children[0];
			var confidence = parseInt(dl.dataset.confidence) || 0;
			var color = dl.dataset.color;

			// Calculate score
			var score = Math.log(Math.max(confidence, 1));
			score -= 3.0 * i;
			score -= 1.0 * j;
			score -= 0.1 * k;
			score -= 0.1 * m;
			score -= 3.0 * n;
			score *= fact.offsetTop < 1 ? 0.5 : 1.0;
			score *= card.dataset.folded == "true" ? 0.5 : 1.0;

			// Initialize candidate record
			var id = source.getAttribute("href");
			var candidate = candidates[id];
			if (candidate === undefined) {
				candidate = candidates[id] = {
					origin: source,
					score: 0,
					confidence: confidence,
					color: color,
					edges: []
				};
			}

			// Update candidate
			candidate.score += score;
			candidate.edges.push(fact);
			if (candidate.confidence < confidence) {
				candidate.confidence = confidence;
				candidate.color = color;
			}
		};

		// Super nasty DFS ;-P
		var cards = document.querySelectorAll(".card[data-type=fact]");
		for (var i = 0; i < cards.length; i++) {
			var card = cards[i];
			var sections = card.querySelectorAll("section[data-scope]");
			for (var j = 0; j < sections.length; j++) {
				var section = sections[j];
				var facts = section.querySelectorAll(".fact");
				for (var k = 0; k < facts.length; k++) {
					var fact = facts[k];
					var contexts = fact.querySelectorAll("ul > li");
					for (var m = 0; m < contexts.length; m++) {
						var context = contexts[m];
						var sources = context.querySelectorAll("a[href]");
						for (var n = 0; n < sources.length; n++) {
							var source = sources[n];
							add(card, section, fact, context, source, i, j, k, m, n);
						}
					}
				}
			}
		}

		// Flatten candidates
		var top = [];
		for (var id in candidates)
			top.push(candidates[id]);

		// Sort by scores
		top.sort(function(a, b) {
			return b.score - a.score;
		});

		// Limit result count
		return top.slice(0, count);
	};

	// Render bibliography
	var render = function(data) {

		// Nothing to render
		var elems = [];
		if (data.length === 0)
			return elems;

		// Bibliography wrapper
		var wrapper = document.createElement("div");
		var h4 = document.createElement("h4");
		var ol = document.createElement("ol");
		wrapper.setAttribute("id", "bibliography");
		h4.setAttribute("class", "fade-in");
		h4.textContent = i18n.bibliographyHeader;
		ol.setAttribute("class", "queue-in");
		wrapper.appendChild(h4);
		wrapper.appendChild(ol);

		// Prepare elements
		for (var i = 0; i < data.length; i++) {
			var record = data[i];
			var li = document.createElement("li");
			var a = document.createElement("a");
			var h5 = document.createElement("h5");
			var div = document.createElement("div");
			var cite = document.createElement("cite");
			li.dataset.confidence = record.confidence;
			li.dataset.color = record.color;
			a.setAttribute("href", record.origin.getAttribute("href"));
			h5.textContent = record.origin.getElementsByTagName("h5")[0].textContent;
			cite.textContent = record.origin.getElementsByTagName("cite")[0].textContent;
			div.appendChild(cite);
			a.appendChild(h5);
			a.appendChild(div);
			li.appendChild(a);
			ol.appendChild(li);
			elems.push(li);

			// Publish date
			if (record.origin.getElementsByTagName("time")[0]) {
				var time = document.createElement("time");
				time.textContent = record.origin.getElementsByTagName("time")[0].textContent;
				div.append(time);
			}
		}

		// Insert to DOM
		right.appendChild(wrapper);
		return elems;
	};

	// Connect to facts
	var connect = function(data, elems) {

		// Nothing to connect
		if (data.length === 0 || elems.length === 0)
			return;

		// Leader line options
		var options = {
			color: window.getComputedStyle(document.getElementById("bibliography")).color,
			endPlug: "disc",
			size: 2,
			startSocket: "left",
			endSocket: "right",
			hide: true
		};

		// Anchor styles
		var styles = {
			paddingTop: null,
			paddingRight: null,
			paddingBottom: null,
			paddingLeft: null,
			cursor: null,
			backgroundColor: null,
			backgroundImage: null,
			backgroundSize: null,
			backgroundPosition: null,
			backgroundRepeat: null
		};

		// Draw leader lines
		data.forEach(function(record, index) {

			// Reference to line instances
			var lines = [];
			var limit = Math.min(record.edges.length, 5);

			// Create anchor
			var anchor = LeaderLine.mouseHoverAnchor(elems[index], "draw", {
				style: styles,
				hoverStyle: styles,
				animOptions: {
					duration: 500
				},
				onSwitch: function(event) {

					// Only respond to entering events
					if (event.type != "mouseenter")
						return;

					// Update lines
					for (var i = 0; i < limit; i++) {
						var line = lines[i];
						var fact = record.edges[i];
						var section = fact.parentNode.parentNode.parentNode;
						var card = section.parentNode.parentNode;

						// Select the best target
						var target = card.dataset.folded == "true" ? card : (fact.offsetTop < 1 ? section : fact);
						line.setOptions({
							end: target,
							dash: target !== fact
						});

						// Redraw the line
						line.position();
					}
				}
			});

			// Create lines
			for (var i = 0; i < limit; i++)
				lines.push(new LeaderLine(anchor, record.edges[i], options));
		});
	};

	// Initialize bibliography
	var initialized = false;
	var init = function() {

		// Do not initialize twice
		if (initialized)
			return;

		// Check visibility of the right column
		if (right.offsetLeft < 1)
			return;

		// Mark as initialized and render it right now
		initialized = true;
		var data = collect(10);
		var elems = render(data);

		// Draw leader lines after a short delay
		// This will prevent lags in SVG animations
		setTimeout(function() {
			connect(data, elems);
		}, 900);
	};

	// We don't have room for the bibliography column on mobile devices
	// But we still need to track the window size since it may start out small on desktop
	// And... there will be more weird devices like the Mate X and Galaxy Fold
	window.addEventListener("resize", init);
	setTimeout(init, 100);
})();

// Ready player one
(function() {

	// Check support of local storage and typed array
	// We use a fixed length Uint8Array as the key buffer
	if (!window.localStorage || !window.ArrayBuffer)
		return;

	// Ring buffer for key strokes
	var ring = new Uint8Array(10);
	var ptr = -1;
	var store = window.localStorage;

	// Reversed DJB2 hashing for a given size
	var rewind = function(size) {
		var h = 5381;
		for (var i = 0, l = ring.length; i < size; i++)
			h = (h * 33) ^ ring[(ptr - i + l) % l];
		return h >>> 0;
	};

	// Listen for strokes
	window.addEventListener("keydown", function(event) {
		ring[ptr = (ptr + 1) % ring.length] = event.keyCode;

		// For debugging only, do the right things and do things right, cheers!
		if (event.keyCode === 0x41 && rewind(10) === 0x6b040f26) {
			store.setItem("konami", store.getItem("konami") == "30" ? "0" : "30");
			window.location.reload(false);
		}
	});
})();

// Embedded arguments
(function() {
	var args = window.args = Object.create(null);
	var hash = window.location.hash.substr(1);
	var kvs = hash.split(";");
	for (var i = 0; i < kvs.length; i++) {
		var kv = kvs[i].split("=");
		switch (kv[0].trim()) {
			case "theme":
				args.theme = (kv[1] || "").trim();
				break;
		}
	}
})();

// Theme Switcher
(function() {
	var DARK_STYLE = "/assets/styles/dark.css";
	var LIGHT_STYLE = "/assets/styles/light.css"
	var toggler = document.getElementById("theme-toggler");
	var head = document.getElementsByTagName("head")[0];
	var link = document.createElement("link");
	link.id = "theme-style"
	link.rel = "stylesheet";
	if ((window.args && window.args.theme == "light") || window.localStorage.getItem("magi-theme") == "light") {
		toggler.checked = true;
		link.href = LIGHT_STYLE;
	} else {
		toggler.checked = false;
		link.href = DARK_STYLE;
	}
	head.appendChild(link);
	head.removeChild(document.getElementById("dark-theme-style"));
	head.removeChild(document.getElementById("light-theme-style"));

	toggler.addEventListener("click", function() {
		var link = document.getElementById("theme-style");
		var href = link.getAttribute("href");
		if (href == DARK_STYLE) {
			link.setAttribute("href", LIGHT_STYLE);
			toggler.checked = true;
			window.localStorage.setItem("magi-theme", "light");
		} else {
			link.setAttribute("href", DARK_STYLE);
			toggler.checked = false;
			window.localStorage.setItem("magi-theme", "dark");
		}
	});
})();