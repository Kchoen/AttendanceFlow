import webview

webview.settings['ALLOW_DOWNLOADS'] = True
webview.create_window('簽到報表匯出系統', 'app.html', confirm_close=True)
webview.start()
