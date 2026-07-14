class Page:
    def __init__(self, name="", next=None, prev=None):
        self.name = name
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root_page = Page(homepage)
        self.current_page = self.root_page
        self.number_of_pages = 1
        

    def visit(self, url: str) -> None:
        new_page = Page(name=url, prev=self.current_page)
        self.current_page.next = new_page
        self.current_page = self.current_page.next
        self.number_of_pages += 1
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current_page.prev != None:
                self.current_page = self.current_page.prev
        
        return self.current_page.name
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current_page.next != None:
                self.current_page = self.current_page.next
        
        return self.current_page.name
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)