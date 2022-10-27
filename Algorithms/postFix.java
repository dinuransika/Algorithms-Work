import java.util.Stack;

public class postFix {
    static int evaluate(String postFixExpression){
        Stack <Integer> stack = new Stack<Integer>();
        String[] tokens = postFixExpression.split(" ");
        for(int i=0; i<tokens.length ; i++){
            if(tokens[i].equals("+")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num1+num2);
            }
            else if(tokens[i].equals("-")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num2-num1);
            }
            else if(tokens[i].equals("*")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num1*num2);
            }
            else if(tokens[i].equals("/")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num2/num1);
            }
            else{
                stack.push(Integer.parseInt(tokens[i]));
            }
        }
        return stack.pop();
    }
    public static void main(String[] args) {
        String postFixExpression = "5 1 2 + 4 * + 3 -";
        System.out.println(evaluate(postFixExpression));
    }
}
