class StackList:
    def _init_(self):
        self.stack_data = list()

    def push(self, new_data):
        self.stack_data.append(new_data)

    def top(self):
        if len(self.stack_data) == 0:
            return None
        else:
            return self.stack_data[-1]

    def pop(self):
        if len(self.stack_data) == 0:
            return None
        else:
            pop_data = self.stack_data.pop()
            return pop_data

    def size(self):
        return len(self.stack_data)


class UndoRedo:
    def _init_(self):
        self.mainStack = StackList()
        self.backupStack = StackList()

    def write(self, data):
        self.mainStack.push(data)
        self.backupStack.push(data)
        print(f"Data {data} berhasil ditambahkan!")

    def undo(self):
        self.mainStack.pop()
        self.printInfo() 

    def redo(self):
        print(''.join(self.backupStack.stack_data))

    def printInfo(self):
        print(''.join(self.mainStack.stack_data))


if _name_ == '_main_':
    obj_undoredo = UndoRedo() 
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.write('Pada Suatu Hari hiduplah seorang kakek-kakek')
    obj_undoredo.write("Dia tinggal sebatang kara di pegunungan")
    obj_undoredo.write("Dia kemudian turun gunung buat kuliah")
    obj_undoredo.write("SEMESTER 5 BANYAK TUGASSSSSSS !!!")
    obj_undoredo.printInfo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.redo()
    obj_undoredo.redo()