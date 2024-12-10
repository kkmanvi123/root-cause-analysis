public class NullDereferenceExample {
    public static void main(String[] args) {
        // Create a String reference but don't initialize it
        String uninitializedString = null;

        // Attempt to call a method on the null reference
        // This will cause a NullPointerException
        int length = uninitializedString.length();

        // This line will not be executed due to the exception above
        System.out.println("The length of the string is: " + length);
    }
}

