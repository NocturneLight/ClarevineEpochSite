// Runs the following code when the page has fully loaded.
window.onload = function () {
    // If the user clicks anywhere on the initial webpage, redirect to the home page.
    if (window.location.pathname == "/")
        document.addEventListener("click", function () { window.location = "/home" })
}