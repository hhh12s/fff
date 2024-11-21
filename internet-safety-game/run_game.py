import http.server
import socketserver
import webbrowser

PORT = 8000

# Запуск локального веб-сервера
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "game.html"
        return super().do_GET()

# Автоматически открываем браузер с игрой
print(f"Игра запущена! Откройте в браузере: http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
