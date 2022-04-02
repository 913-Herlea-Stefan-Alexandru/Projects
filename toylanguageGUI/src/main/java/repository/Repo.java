package repository;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyList;

public class Repo implements IRepo {
	
	private List<PrgState> prgList;
	private String fileName;
	
	public Repo(PrgState prg, String fileName) {
		prgList = new ArrayList<PrgState>();
		prgList.add(prg);
		this.fileName = fileName;
		try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.fileName)))) {
			logFile.write("");
			logFile.flush();
			logFile.close();
		} catch (IOException e) {
			throw new MyException("Cannot open file " + this.fileName);
		}
	}
	
	public Repo(String fileName) {
		prgList = new ArrayList<PrgState>();
		this.fileName = fileName;
		try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.fileName)))) {
			logFile.write("");
			logFile.flush();
			logFile.close();
		} catch (IOException e) {
			throw new MyException("Cannot open file " + this.fileName);
		}
	}
	
	public Repo() {
		prgList = new ArrayList<PrgState>();
		this.fileName = "";
	}
	
	public PrgState getPrg(int number) {
		return prgList.get(number);
	}

	public PrgState getPrgById(int id) {
		for (PrgState prg: prgList) {
			if (prg.getStateId() == id) {
				return prg;
			}
		}
		return null;
	}
	
	@Override
	public void logProgramState(PrgState program) throws MyException {
		try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.fileName, true)))) {
			logFile.write(program.toString());
			logFile.write("----------------------------------------------------------\n");
			logFile.flush();
			logFile.close();
		} catch (IOException e) {
			throw new MyException("Cannot open file " + this.fileName);
		}
		
	}

	@Override
	public List<PrgState> getPrgList() {
		return prgList;
	}

	@Override
	public void setPrgList(List<PrgState> prgList) {
		this.prgList = prgList;
	}

}
