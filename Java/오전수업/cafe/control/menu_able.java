package cafe.control;

@FunctionalInterface
public interface menu_able {
	
	public boolean menu_active();
	
}

// 인터페이스 - 추상 클래스의 하나
// 추상 클래스는 추상 메서드를 가지고 있는 클래스이다.
// 추상 클래스는 객체 생성에 제한이 있다.
// 고로 인터페이스는 추상메서드를 가지며, 객체 생성에 제한이 있다.
// 인터페이스에 정의하는 메서드는 기본적으로 추상메서드로 정의된다.
// 인터페이스에는 인스턴스변수, 인스턴스메서드 정의 불가; 