package repository;

import java.util.List;

import exceptions.MyException;
import model.PrgState;

public interface IRepo {
	
	void logProgramState(PrgState program) throws MyException;
	
	List<PrgState> getPrgList();

	PrgState getPrgById(int id);
	
	void setPrgList(List<PrgState> prgList);
}
