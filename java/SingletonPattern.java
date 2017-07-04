public class EagerInitialised {

    private static final EagerInitialised eagerInitialised = new EagerInitialised();

    private EagerInitialised() {}

    public static final EagerInitialised getInstance() {
        return this.eagerInitialised;
    }
}
