public class OOPLinkedListElement {
    private int value;
    private OOPLinkedListElement next;

    public OOPLinkedListElement(int value) {
        this.value = value;
        this.next = null;
    }

    public OOPLinkedListElement(int value, OOPLinkedListElement next) {
        this.value = value;
        this.next = next;
    }

    public OOPLinkedListElement getNext() {
        return next;
    }

    public void setNext(OOPLinkedListElement next) {
        this.next = next;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

}
