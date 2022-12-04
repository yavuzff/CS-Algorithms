import java.util.NoSuchElementException;

public class OOPLinkedList {
    protected OOPLinkedListElement head;

    public OOPLinkedList() {
        this.head = null;
    }

    public OOPLinkedList(int headValue) {
        this.head = new OOPLinkedListElement(headValue,null);
    }

    public int getHead() throws NoSuchElementException{
        if (head==null) {
            throw new NoSuchElementException("The linked list is empty!");
        }
        return head.getValue();
    }

    public void addElement (int value){
        OOPLinkedListElement oldHead = head;
        head = new OOPLinkedListElement(value,oldHead);
    }

    public void removeElement () throws NoSuchElementException {
        if (head == null){
            throw new NoSuchElementException("The linked list is empty!");
        }
        head = head.getNext();
    }

    public int getNth(int n) throws IllegalArgumentException{
        if (n<1 || head == null) {
            throw new IllegalArgumentException("n out of bounds.");
        }
        OOPLinkedListElement current = head;
        for (int i=1;i<n;i++){
            current = current.getNext();
            if (current == null){
                throw new IllegalArgumentException("n out of bounds.");
            }

        }
        return current.getValue();
    }

    public int length(){
        //if (head==null){
        //    return 0;
        //}
        int length = 0;
        OOPLinkedListElement current = head;
        while (current != null){
            current = current.getNext();
            length += 1;
        }
        return length;
    }
}
