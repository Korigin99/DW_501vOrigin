package cafe.control;

public class Exit implements menu_able{

	@Override
	public boolean menu_active() {
		System.out.println("안녕히가세요~");
		return false;
	}

}
