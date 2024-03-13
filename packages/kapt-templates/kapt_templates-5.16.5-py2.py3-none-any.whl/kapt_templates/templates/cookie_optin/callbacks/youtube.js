function (consent, app) {
  var cookieNotices = document.querySelectorAll('[data-cookieoptin]')

  if (consent === false) {
    for (var i = 0; i < cookieNotices.length; i++) {
      var cookieNotice = cookieNotices[i];

      if (cookieNotice.parentElement.classList.contains('cookieoptin')) {
        /* .video-player is the direct parent of cookie notice */
      } else {
        /* .video-player is a sibling of cookie notice */
        var videoDiv = cookieNotice.parentElement.parentElement
        var div = videoDiv.querySelector('.video-player')

        /* Move cookieNotice inside .video-player */
        cookieNotice.parentElement.removeChild(cookieNotice)
        cookieNotice.classList.remove('cookieoptin-hide')
        div.innerHTML = cookieNotice.outerHTML + div.innerHTML

        div.querySelector('.btn').addEventListener('click', function (e) {
          e.preventDefault()
          cookieNotice.className += ' cookieoptin-hide'
          klaro.getManager(klaroConfig).updateConsent(app.name, true)
          klaro.getManager(klaroConfig).saveAndApplyConsents()
          document.location.reload()
        })
      }
    }
  } else {
    for (var i = 0; i < cookieNotices.length; i++) {
      var cookieNotice = cookieNotices[i];
      cookieNotice.className += ' cookieoptin-hide'
    }

    var fitVids = require('fitvids')
    fitVids({
      players: 'iframe[src*="dailymotion.com"]'
    })
  }
}

