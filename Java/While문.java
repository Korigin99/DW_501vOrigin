package 자바0913;

public class While문 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int count = 0;
		while (true) {
			count++;
			System.out.println("안녕?");
			if (count == 20) {
				break;
			}
		}
		int n = 0;
		int sum = 0;
		while (true) {
			++n;
			sum += n;
			if (n == 55) {
				break;
			}
		}
		System.out.println(n);
	}

}
