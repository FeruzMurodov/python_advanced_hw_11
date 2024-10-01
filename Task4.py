class Stack:
    def __init__(self):
        self.__stack = list()

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]

    def __str__(self):
        line = ''
        for item in self.__stack:
            line += item
        return line


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def new_task(self, task: str, priority: int):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def remove_task(self, text):

        for stack in self.tasks.values():
            temp_stack = Stack()
            while not stack.is_empty():
                print('flag')
                task = stack.pop()
                if task != text:
                    temp_stack.push(task)

            while not temp_stack.is_empty():
                print('flag2')
                stack.push(temp_stack.pop())
            #print(stack.is_empty())

    def __str__(self):
        sorted_keys = sorted(self.tasks.keys())
        out = []
        for key in sorted_keys:
            task_line = [str(key)]
            temp_stack = Stack()
            while not self.tasks[key].is_empty():
                task = self.tasks[key].pop()
                temp_stack.push(task)
            while not temp_stack.is_empty():
                task_line.append(temp_stack.pop())
            out.append(' '.join(task_line))
        return '\n'.join(out)


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.new_task("сделать уборку", 4)
    task_manager.new_task("помыть посуду", 4)
    task_manager.new_task("отдохнуть", 1)
    task_manager.new_task("поесть", 2)
    task_manager.new_task("сдать ДЗ", 2)
    print(task_manager)
