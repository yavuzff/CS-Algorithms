import java.util.Arrays;

public class BinaryMinHeap {
    private int[] heap;
    private int size;

    public BinaryMinHeap(int capacity){
        this.heap = new int[capacity];
        this.size = 0;
    }

    public int extract (){
        if (size == 0){
            throw new RuntimeException("Heap is empty!");
        }
        int item = heap[0];
        size = size - 1;
        heap[0] = heap[size]; //place last element to root
        siftdown(0);
        return item;
    }

    public void insert(int item){
        if (size == heap.length){
            throw new RuntimeException("Heap is full!");
        }
        heap[size] = item;
        size += 1;
        siftup(size-1);
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public boolean isFull(){
        return size == heap.length;
    }

    private void siftdown(int i){
        int i1 = left(i);
        int i2 = right(i);
        if (i1 < size){ //at least 1 child exists
            if (i2 >= size){ //1 child exists
                if (heap[i1] < heap[i]){ //swap if out of order
                    swap(i,i1);
                }
            }
            else { //both children exist
                if (heap[i] <= heap[i1] && heap[i] <= heap[i2]){ //parent is smallest so is in correct place
                    return;
                } else if (heap[i1] <= heap[i] && heap[i1] <= heap[i2]){ //left is smallest
                    swap(i,i1);
                    siftdown(i1);
                } else { //right is smallest
                    swap(i,i2);
                    siftdown(i2);
                }
            }
        }
    }

    private void siftup (int i){
        if (i == 0){ //root
            return;
        }
        int ip = parent(i);
        if (heap[i] < heap[ip]){
            swap(i,ip);
            siftup(ip);
        }
    }

    private int left (int i){
        return 2*i + 1;
    }
    private int right (int i){
        return 2*i + 2;
    }
    private int parent (int i){
        return (i-1)/2;
    }

    private void swap (int i, int j){
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    @Override
    public String toString() {
        return "BinaryMinHeap{" +
                "heap=" + Arrays.toString(heap) +
                ", size=" + size +
                '}';
    }
}
