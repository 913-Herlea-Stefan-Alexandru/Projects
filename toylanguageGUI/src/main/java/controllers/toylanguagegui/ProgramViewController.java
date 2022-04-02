package controllers.toylanguagegui;

import controller.Controller;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import model.PrgState;
import model.adt.DictionaryDTO;
import model.adt.MyIList;
import model.adt.SemaphoreDTO;
import model.statements.IStmt;
import model.values.StringValue;
import model.values.Value;
import repository.IRepo;

import java.io.BufferedReader;
import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;
import java.util.concurrent.Executors;

public class ProgramViewController implements Initializable {
    private Controller controller;

    private IRepo repo;

    @FXML
    private ListView<Integer> StatesList;
    @FXML
    private ListView<IStmt> ExeStackList;
    @FXML
    private ListView<Value> OutputList;
    @FXML
    private TableView SymTable;
    @FXML
    private TableColumn<DictionaryDTO<String, Value>, String> SymTableSym;
    @FXML
    private TableColumn<DictionaryDTO<String, Value>, Value> SymTableVal;
    @FXML
    private TableView HeapTable;
    @FXML
    private TableColumn<DictionaryDTO<Integer, Value>, Integer> HeapTableAddr;
    @FXML
    private TableColumn<DictionaryDTO<Integer, Value>, Value> HeapTableVal;
    @FXML
    private TableView SemaphoreTable;
    @FXML
    private TableColumn<SemaphoreDTO, Integer> SemaphoreTableAddress;
    @FXML
    private TableColumn<SemaphoreDTO, Integer> SemaphoreTablePermits;
    @FXML
    private TableColumn<SemaphoreDTO, String> SemaphoreTableStates;
    @FXML
    private TableView FileTable;
    @FXML
    private TableColumn<DictionaryDTO<StringValue, BufferedReader>, BufferedReader> FileTableId;
    @FXML
    private TableColumn<DictionaryDTO<StringValue, BufferedReader>, StringValue> FileTableName;
    @FXML
    private Button RunButton;
    @FXML
    private Button OneStep;

    public void setUp() {
        StatesList.setItems(getPrgStatesId());
        StatesList.getSelectionModel().selectFirst();

        if (StatesList.getItems().isEmpty()) {
            ExeStackList.setItems(FXCollections.observableArrayList());
            OneStep.setDisable(true);
            RunButton.setDisable(true);
        }
        else
            ExeStackList.setItems(getExeStack());

        OutputList.setItems(getOutput());

        SymTableSym.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<String, Value>, String>("key"));
        SymTableVal.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<String, Value>, Value>("value"));
        SymTable.setItems(getSymTable());

        HeapTableAddr.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<Integer, Value>, Integer>("key"));
        HeapTableVal.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<Integer, Value>, Value>("value"));
        HeapTable.setItems(getHeapTable());

        SemaphoreTableAddress.setCellValueFactory(new PropertyValueFactory<SemaphoreDTO, Integer>("address"));
        SemaphoreTablePermits.setCellValueFactory(new PropertyValueFactory<SemaphoreDTO, Integer>("permits"));
        SemaphoreTableStates.setCellValueFactory(new PropertyValueFactory<SemaphoreDTO, String>("states"));
        SemaphoreTable.setItems(getSemaphoreTable());

        FileTableId.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<StringValue, BufferedReader>, BufferedReader>("value"));
        FileTableName.setCellValueFactory(new PropertyValueFactory<DictionaryDTO<StringValue, BufferedReader>, StringValue>("key"));
        FileTable.setItems(getFileTable());
    }

    private ObservableList<Integer> getPrgStatesId() {
        ObservableList<Integer> states = FXCollections.observableArrayList();
        for (PrgState p: repo.getPrgList()) {
            states.add(p.getStateId());
        }
        return states;
    }

    private ObservableList<IStmt> getExeStack() {
        ObservableList<IStmt> exe = FXCollections.observableArrayList();
        PrgState crtPrg = repo.getPrgById(StatesList.getSelectionModel().getSelectedItem());
        exe.addAll(crtPrg.getExeStack().toList());
        return exe;
    }

    private ObservableList<Value> getOutput() {
        ObservableList<Value> out = FXCollections.observableArrayList();
        PrgState prg = repo.getPrgList().get(0);
        MyIList<Value> vList = prg.getOut();
        for (int i = 0; i < vList.size(); i++) {
            out.add(vList.get(i));
        }
        return out;
    }

    private ObservableList<DictionaryDTO<String, Value>> getSymTable() {
        ObservableList<DictionaryDTO<String, Value>> symTbl = FXCollections.observableArrayList();
        PrgState crtPrg = repo.getPrgById(StatesList.getSelectionModel().getSelectedItem());
        symTbl.addAll(crtPrg.getSymTable().getDTOList());
        return symTbl;
    }

    private ObservableList<DictionaryDTO<Integer, Value>> getHeapTable() {
        ObservableList<DictionaryDTO<Integer, Value>> heapTbl = FXCollections.observableArrayList();
        PrgState crtPrg = repo.getPrgById(StatesList.getSelectionModel().getSelectedItem());
        heapTbl.addAll(crtPrg.getHeapTable().getDTOList());
        return heapTbl;
    }

    private ObservableList<SemaphoreDTO> getSemaphoreTable() {
        ObservableList<SemaphoreDTO> heapTbl = FXCollections.observableArrayList();
        PrgState crtPrg = repo.getPrgById(StatesList.getSelectionModel().getSelectedItem());
        heapTbl.addAll(crtPrg.getSemaphoreTable().getDTOList());
        return heapTbl;
    }

    private ObservableList<DictionaryDTO<StringValue, BufferedReader>> getFileTable() {
        ObservableList<DictionaryDTO<StringValue, BufferedReader>> fileTbl = FXCollections.observableArrayList();
        PrgState crtPrg = repo.getPrgById(StatesList.getSelectionModel().getSelectedItem());
        fileTbl.addAll(crtPrg.getFileTable().getDTOList());
        return fileTbl;
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }

    public void setController(Controller ctr) {
        this.controller = ctr;
        this.repo = controller.getRepo();
    }

    private void allStep() {
        controller.executor = Executors.newFixedThreadPool(2);
        //remove the completed programs
        List<PrgState> prgList=controller.removeCompletedPrg(repo.getPrgList());
        while(prgList.size() > 0){
            ///HERE you can call conservativeGarbageCollector
            prgList.get(0).getHeapTable().setContent(controller.unsafeGarbageCollector(
                    controller.getAddrFromSymTable(prgList.get(0).getSymTable().getContent().values()),
                    prgList.get(0).getHeapTable().getContent()));
            controller.oneStepForAllPrg(prgList);
            setUp();
            //remove the completed programs
            prgList=controller.removeCompletedPrg(repo.getPrgList());
        }
        controller.executor.shutdownNow();
        //HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        //setPrgList of repository in order to change the repository
        // update the repository state
        repo.setPrgList(prgList);
    }

    @FXML
    protected void onClick() {
        if (StatesList.getItems().isEmpty()) {
            ExeStackList.setItems(FXCollections.observableArrayList());
            OneStep.setDisable(true);
            RunButton.setDisable(true);
        }
        else
            ExeStackList.setItems(getExeStack());

        SymTable.setItems(getSymTable());
    }

    @FXML
    protected void onRun() {
        try {
            allStep();
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Toy Language - Current program finished");
            alert.setHeaderText("Program finished");
            alert.setContentText("Program successfully finished!");
            alert.showAndWait();
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        OneStep.setDisable(true);
        RunButton.setDisable(true);
    }

    @FXML
    protected void onOneStep() {
        if (controller.executor == null) {
            controller.executor = Executors.newFixedThreadPool(2);
        }
        RunButton.setDisable(true);

        List<PrgState> prgList=controller.removeCompletedPrg(repo.getPrgList());
        try {
            prgList.get(0).getHeapTable().setContent(controller.unsafeGarbageCollector(
                    controller.getAddrFromSymTable(prgList.get(0).getSymTable().getContent().values()),
                    prgList.get(0).getHeapTable().getContent()));
            controller.oneStepForAllPrg(prgList);
            setUp();
            //remove the completed programs
            prgList=controller.removeCompletedPrg(repo.getPrgList());
        }
        catch (Exception ex) {
            OneStep.setDisable(true);
            controller.executor.shutdownNow();
            repo.setPrgList(prgList);
            StatesList.setItems(getPrgStatesId());
            StatesList.getSelectionModel().selectFirst();
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Toy Language - Current program finished");
            alert.setHeaderText("Program finished");
            alert.setContentText("Program successfully finished!");
            alert.showAndWait();
        }
    }
}
