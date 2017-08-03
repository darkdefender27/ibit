package bst.model;

/**
 * Created by shubhamutwal on 03/08/17.
 */
public class Node {

    private Integer value;
    private Node left;
    private Node right;

    public Node(Integer value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setRight(Node right) {
        this.right = right;
    }

    public Integer getValue() {
        return value;
    }

    public Node getLeft() {
        return left;
    }

    public Node getRight() {
        return right;
    }
}
