class heap():
    # Parameter 'type' can take two values -- "MIN" and "MAX"
    def __init__(this, type):
        this.main_array = []
        this.type = type

    def insert(this, data):
        
        this.main_array.append(data)
        heap_size = len(this.main_array)
        # decreasing current heap size
        current = (heap_size-1)
        parent = (current-1)//2
        while(current>0):
            curr_value = this.main_array[current]
            parent_value = this.main_array[parent]
            if(this.type == 'MIN' and curr_value < parent_value):
                this.main_array[current], this.main_array[parent] = this.main_array[parent], this.main_array[current]
                current=parent
            elif(this.type == 'MAX' and curr_value > parent_value):
                this.main_array[current], this.main_array[parent] = this.main_array[parent], this.main_array[current]
                current=parent
            else:
                break
            parent=(current-1)//2
    



