package controller;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyIStack;
import model.statements.IStmt;
import model.values.RefValue;
import model.values.Value;
import repository.IRepo;

public class Controller {
	private IRepo repo;
	private boolean displayFlag;
	public ExecutorService executor;
	private String showController;
	
	public Controller(IRepo repo, boolean flag) {
		this.repo = repo;
		this.displayFlag = flag;
		MyIStack<IStmt> stk = repo.getPrgList().get(0).getExeStack();
		IStmt stmt = stk.pop();
		stk.push(stmt);
		this.showController = stmt.toString();
	}
	
	public boolean getDisplayFlacg() {
		return this.displayFlag;
	}
	
	public void setDisplayFlag(boolean newFlag) {
		this.displayFlag = newFlag;
	}
	
	public List<Integer> getAddrFromSymTable(Collection<Value> symTableValues){
		return symTableValues.stream()
			.filter(v-> v instanceof RefValue)
			.map(v-> {RefValue v1 = (RefValue)v; return v1.getAddr();})
			.collect(Collectors.toList());
	}
	
	private boolean filterFct(List<Integer> symTableAddr, Set<Entry<Integer, Value>> heap, Entry<Integer, Value> e) {
		if (symTableAddr.contains(e.getKey()))
			return true;
		Iterator<Entry<Integer, Value>> it = heap.iterator();
		while (it.hasNext()) {
			Entry<Integer, Value> elem = it.next();
			if (e.equals(elem)) {
				continue;
			}
			if (elem.getValue() instanceof RefValue) {
				RefValue el = (RefValue) elem.getValue();
				if (el.getAddr() == e.getKey()) {
					boolean rec = filterFct(symTableAddr, heap, elem);
					if (rec)
						return true;
				}
			}
		}
		return false;
	}
	
	public Map<Integer,Value> unsafeGarbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap){
		return heap.entrySet().stream()
			.filter(e-> filterFct(symTableAddr, heap.entrySet(), e))
			.collect(Collectors.toMap(Entry::getKey, Entry::getValue));
	}

	public IRepo getRepo() {
		return repo;
	}
	
	public void allStep() {    
		executor = Executors.newFixedThreadPool(2);    
		//remove the completed programs    
		List<PrgState>  prgList=removeCompletedPrg(repo.getPrgList());    
		while(prgList.size() > 0){
			///HERE you can call conservativeGarbageCollector
			prgList.get(0).getHeapTable().setContent(unsafeGarbageCollector(
					getAddrFromSymTable(prgList.get(0).getSymTable().getContent().values()),
					prgList.get(0).getHeapTable().getContent()));
			oneStepForAllPrg(prgList);
			//remove the completed programs             
			prgList=removeCompletedPrg(repo.getPrgList());  
		}     
		executor.shutdownNow();     
		//HERE the repository still contains at least one Completed Prg     
		// and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method     
		//setPrgList of repository in order to change the repository    
		// update the repository state     
		repo.setPrgList(prgList);  
	} 
	
	public void oneStepForAllPrg(List<PrgState> prgList){
		prgList.forEach(prg -> repo.logProgramState(prg));
		
		List<Callable<PrgState>> callList = prgList.stream()
				.map((PrgState p) -> (Callable<PrgState>)(() -> {return p.oneStep();}))
				.collect(Collectors.toList());
		
		List<PrgState> newPrgList = new ArrayList<>();
		try {
			newPrgList = executor.invokeAll(callList).stream()
							.map(future -> { try {
											 	 return future.get();
											 }
											 catch(MyException e) {
												 System.out.println(e.getMessage());
											 } catch (InterruptedException e) {
												 System.out.println(e.getMessage());
											} catch (ExecutionException e) {
												System.out.println(e.getMessage());
											}
											return null;
										   }
								)
							.filter(p -> p!=null)
							.collect(Collectors.toList());
		} catch (InterruptedException e) {
			System.out.println(e.getMessage());
		}
		
		prgList.addAll(newPrgList);
		
		prgList.forEach(prg -> repo.logProgramState(prg));
		repo.setPrgList(prgList);
	}
	
	public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList) {
		return inPrgList.stream()
				.filter(p -> p.isNotCompleted())
				.collect(Collectors.toList());
	}

	@Override
	public String toString() {
		return this.showController;
	}
}
