function (consent, app) {
  if (consent === false) {
    var elements = document.querySelectorAll('[data-cookieoptin-addthis]')
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      element.classList.remove('cookieoptin-hide')

      element.querySelector('.btn').addEventListener('click', function (e) {
        e.preventDefault()
        element.className += ' cookieoptin-hide'
        klaro.getManager().updateConsent(app.name, true)
        klaro.getManager().saveAndApplyConsents()
        document.location.reload()
      })
    }
  }
}
