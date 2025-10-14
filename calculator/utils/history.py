class HistoryManager:
    
    def __init__(self, max_size=100):
        self.history = []
        self.max_size = max_size
        self.current_index = -1
    
    def add(self, expression, result):
        entry = {
            'expression': expression,
            'result': result
        }
        self.history.append(entry)
        
        if len(self.history) > self.max_size:
            self.history.pop(0)
        
        self.current_index = len(self.history) - 1
    
    def get_last(self, n=1):
        if n <= 0:
            return []
        return self.history[-n:]
    
    def get_all(self):
        return self.history.copy()
    
    def clear(self):
        self.history = []
        self.current_index = -1
    
    def get_by_index(self, index):
        if 0 <= index < len(self.history):
            return self.history[index]
        else:
            return None
    
    def navigate_up(self):
        if self.current_index > 0:
            self.current_index -= 1
        return self.get_current()
    
    def navigate_down(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
        return self.get_current()
    
    def get_current(self):
        if 0 <= self.current_index < len(self.history):
            return self.history[self.current_index]
        return None
    
    def get_count(self):
        return len(self.history)


history_manager = HistoryManager()

def add_to_history(expression, result):
    history_manager.add(expression, result)

def get_history(n=10):

    return history_manager.get_last(n)

def clear_history():
    history_manager.clear()
    return "History cleared"

def history_count():
    return history_manager.get_count()


HISTORY_FUNCTIONS = {
    'history': get_history,
    'hist': get_history,
    'clear_history': clear_history,
    'clear_hist': clear_history,
    'history_count': history_count,
}

def get_function(name):
    if name in HISTORY_FUNCTIONS:
        return HISTORY_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown history function: {name}")