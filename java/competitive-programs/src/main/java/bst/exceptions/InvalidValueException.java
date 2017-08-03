package bst.exceptions;

/**
 * Created by shubhamutwal on 03/08/17.
 */
public class InvalidValueException extends RuntimeException {

    public InvalidValueException(String message) {
        super(message);
    }

    @Override
    public String getMessage() {
        return super.getMessage();
    }
}
