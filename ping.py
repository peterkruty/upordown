import rumps
import ping3
import threading
import time

class PingToolbarApp(rumps.App):
    def __init__(self, target):
        super(PingToolbarApp, self).__init__("Ping Status")
        self.target = target
        self.icon = "red.png"  # Start with red icon
        self.ping_status = False
        self.ping_history = []  # List to keep track of last 30 ping replies
        self.update_thread = threading.Thread(target=self.ping_target)
        self.update_thread.daemon = True
        self.update_thread.start()

        # Add a menu item to show the ping history
        self.menu = ["Full Ping History"]

    @rumps.clicked("Full Ping History")
    def show_full_ping_history(self, _):
        history_str = "\n".join(self.ping_history)
        rumps.alert(title="Full Ping History", message=history_str)

    def ping_target(self):
        while True:
            response = ping3.ping(self.target, timeout=1)
            if response is not None:
                self.ping_status = True
                self.icon = "green.png"
                self.ping_history.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - UP ({response * 1000:.2f} ms)")
            else:
                self.ping_status = False
                self.icon = "red.png"
                self.ping_history.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - DOWN")

            # Limit history to the last 30 entries
            if len(self.ping_history) > 30:
                self.ping_history.pop(0)

            self.title = "UP" if self.ping_status else "DOWN"
            time.sleep(1)

if __name__ == "__main__":
    target_host = "8.8.8.8"  # Change to your desired target host or IP
    app = PingToolbarApp(target_host)
    app.run()
