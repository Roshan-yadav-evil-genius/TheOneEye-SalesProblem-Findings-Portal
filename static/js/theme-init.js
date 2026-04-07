(function () {
  var STORAGE_KEY = "theme"
  var COLOR_SCHEME_QUERY = "(prefers-color-scheme: dark)"

  function getStored() {
    var v = localStorage.getItem(STORAGE_KEY)
    if (v === "light" || v === "dark" || v === "system") {
      return v
    }
    return "system"
  }

  function resolve(stored) {
    if (stored === "light" || stored === "dark") {
      return stored
    }
    return window.matchMedia(COLOR_SCHEME_QUERY).matches ? "dark" : "light"
  }

  function apply() {
    var stored = getStored()
    var resolved = resolve(stored)
    var root = document.documentElement
    root.classList.remove("light", "dark")
    root.classList.add(resolved)
    root.dataset.themeStored = stored
    root.dataset.themeResolved = resolved
    try {
      document.dispatchEvent(
        new CustomEvent("portalthemechange", {
          detail: { stored: stored, resolved: resolved },
        })
      )
    } catch (_) {}
  }

  function setTheme(next) {
    if (next !== "light" && next !== "dark" && next !== "system") {
      return
    }
    localStorage.setItem(STORAGE_KEY, next)
    apply()
  }

  function cycleTheme() {
    var s = getStored()
    if (s === "system") {
      setTheme("light")
    } else if (s === "light") {
      setTheme("dark")
    } else {
      setTheme("system")
    }
  }

  apply()

  window.matchMedia(COLOR_SCHEME_QUERY).addEventListener("change", function () {
    if (getStored() === "system") {
      apply()
    }
  })

  window.addEventListener("storage", function (event) {
    if (event.key === STORAGE_KEY) {
      apply()
    }
  })

  window.PortalTheme = {
    setTheme: setTheme,
    getStored: getStored,
    getResolved: function () {
      return resolve(getStored())
    },
    cycle: cycleTheme,
  }
})()
