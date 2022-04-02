package controllers.toylanguagegui;

import controller.Controller;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;
import model.PrgState;
import model.adt.*;
import model.expressions.*;
import model.statements.*;
import model.types.*;
import model.values.IntValue;
import model.values.StringValue;
import model.values.Value;
import repository.IRepo;
import repository.Repo;

import java.io.BufferedReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;

public class HelloController implements Initializable {
    @FXML
    private Button LaunchButton;
    @FXML
    private ListView<Controller> ProgramList;

    private void setUp() {
        Controller ctr1 = null;
        Controller ctr2 = null;
        Controller ctr3 = null;
        Controller ctr4 = null;
        Controller ctr5 = null;
        Controller ctr6 = null;
        Controller ctr7 = null;
        Controller ctr8 = null;
        Controller ctr9 = null;
        Controller ctr10 = null;
        Controller ctr11 = null;
        Controller ctr12 = null;
        Controller ctr13 = null;
        Controller ctr14 = null;
        Controller ctr15 = null;

        String err = "";

        /*
        IStmt ex1 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))));
        ex1.typecheck(new MyDictionary<String, Type>());
        PrgState prg1 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex1);
        IRepo repo1 = new Repo(prg1,"log1.txt");
        ctr1 = new Controller(repo1, false);

        IStmt ex2 = new CompStmt( new VarDeclStmt("a",new IntType()),
                new CompStmt(new VarDeclStmt("b",new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp('+',new ValExp(new IntValue(2)),new ArithExp('*',new ValExp(new IntValue(3)), new ValExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new ValExp(new IntValue(1)))),
                                        new PrintStmt(new VarExp("b"))))));
        ex2.typecheck(new MyDictionary<String, Type>());
        PrgState prg2 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex2);
        IRepo repo2 = new Repo(prg2,"log2.txt");
        ctr2 = new Controller(repo2, false);

        IStmt ex3 = new CompStmt(new VarDeclStmt("a",new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new VarExp("a"),
                                        new AssignStmt("v",new ValExp(new IntValue(2))),
                                        new AssignStmt("v", new ValExp(new IntValue(3)))),
                                        new PrintStmt(new VarExp("v"))))));
        ex3.typecheck(new MyDictionary<String, Type>());
        PrgState prg3 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex3);
        IRepo repo3 = new Repo(prg3,"log3.txt");
        ctr3 = new Controller(repo3, false);

        IStmt ex4 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf", new ValExp(new StringValue("test.in"))),
                        new CompStmt(new OpenRFileStmt(new VarExp("varf")),
                                new CompStmt(new VarDeclStmt("varc",new IntType()),
                                        new CompStmt(new ReadFileStmt(new VarExp("varf"),"varc"),
                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new ReadFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                                        new CloseRFileStmt(new VarExp("varf"))))))))));
        ex4.typecheck(new MyDictionary<String, Type>());
        PrgState prg4 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex4);
        IRepo repo4 = new Repo(prg4,"log4.txt");
        ctr4 = new Controller(repo4, false);

        IStmt ex5 = new CompStmt(new VarDeclStmt("a", new IntType()),
                new CompStmt(new AssignStmt("a", new ValExp(new IntValue(11))),
                        new IfStmt(new RelExpr("<=", new VarExp("a"), new ValExp(new IntValue(15))),
                                new PrintStmt(new ValExp(new BoolValue(true))),
                                new PrintStmt(new ValExp(new BoolValue(false))))));
        ex5.typecheck(new MyDictionary<String, Type>());
        PrgState prg5 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex5);
        IRepo repo5 = new Repo(prg5,"log5.txt");
        ctr5 = new Controller(repo5, false);

        IStmt ex6 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocStmt("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new VarExp("v")),
                                                new PrintStmt(new VarExp("a")))))));
        ex6.typecheck(new MyDictionary<String, Type>());
        PrgState prg6 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex6);
        IRepo repo6 = new Repo(prg6,"log6.txt");
        ctr6 = new Controller(repo6, false);

        IStmt ex7 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocStmt("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new HeapReadExp(new VarExp("v"))),
                                                new PrintStmt(new ArithExp('+', new HeapReadExp(new HeapReadExp(new VarExp("a"))), new ValExp(new IntValue(5)))))))));
        ex7.typecheck(new MyDictionary<String, Type>());
        PrgState prg7 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex7);
        IRepo repo7 = new Repo(prg7,"log7.txt");
        ctr7 = new Controller(repo7, false);

        IStmt ex8 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(20))),
                        new CompStmt(new PrintStmt(new HeapReadExp(new VarExp("v"))),
                                new CompStmt(new HeapWriteStmt("v", new ValExp(new IntValue(30))),
                                        new PrintStmt(new ArithExp('+', new HeapReadExp(new VarExp("v")), new ValExp(new IntValue(5))))))));
        ex8.typecheck(new MyDictionary<String, Type>());
        PrgState prg8 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex8);
        IRepo repo8 = new Repo(prg8,"log8.txt");
        ctr8 = new Controller(repo8, false);

        IStmt ex9 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocStmt("a", new VarExp("v")),
                                        new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(30))),
                                                new CompStmt(new PrintStmt(new VarExp("v")),
                                                        new PrintStmt(new HeapReadExp(new HeapReadExp(new VarExp("a"))))))))));
        ex9.typecheck(new MyDictionary<String, Type>());
        PrgState prg9 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex9);
        IRepo repo9 = new Repo(prg9,"log9.txt");
        ctr9 = new Controller(repo9, false);

        IStmt ex10 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelExpr(">", new VarExp("v"), new ValExp(new IntValue(0))),
                                new CompStmt(new PrintStmt(new VarExp("v")),
                                        new AssignStmt("v", new ArithExp('-', new VarExp("v"), new ValExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));
        ex10.typecheck(new MyDictionary<String, Type>());
        PrgState prg10 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex10);
        IRepo repo10 = new Repo(prg10,"log10.txt");
        ctr10 = new Controller(repo10, false);

        IStmt ex11 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocStmt("a", new VarExp("v")),
                                        new CompStmt(new HeapAllocStmt("v", new ValExp(new IntValue(30))),
                                                new CompStmt(new PrintStmt(new VarExp("v")),
                                                        new CompStmt(new PrintStmt(new HeapReadExp(new HeapReadExp(new VarExp("a")))),
                                                                new CompStmt(new HeapAllocStmt("a", new VarExp("v")),
                                                                        new PrintStmt(new HeapReadExp(new HeapReadExp(new VarExp("a"))))))))))));
        ex11.typecheck(new MyDictionary<String, Type>());
        PrgState prg11 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex11);
        IRepo repo11 = new Repo(prg11,"log11.txt");
        ctr11 = new Controller(repo11, false);

        IStmt ex12 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                        new CompStmt(new AssignStmt("v", new ValExp(new IntValue(10))),
                                new CompStmt(new HeapAllocStmt("a", new ValExp(new IntValue(22))),
                                        new CompStmt(new ForkStmt(new CompStmt(new HeapWriteStmt("a", new ValExp(new IntValue(30))),
                                                new CompStmt(new AssignStmt("v", new ValExp(new IntValue(32))),
                                                        new CompStmt(new PrintStmt(new VarExp("v")),
                                                                new PrintStmt(new HeapReadExp(new VarExp("a"))))))),
                                                new CompStmt(new PrintStmt(new VarExp("v")),
                                                        new PrintStmt(new HeapReadExp(new VarExp("a")))))))));
        ex12.typecheck(new MyDictionary<String, Type>());
        PrgState prg12 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex12);
        IRepo repo12 = new Repo(prg12,"log12.txt");
        ctr12 = new Controller(repo12, false);

        IStmt ex13 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValExp(new BoolValue(true))),
                        new PrintStmt(new VarExp("v"))));
        try {
            ex13.typecheck(new MyDictionary<String, Type>());
            PrgState prg13 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex13);
            IRepo repo13 = new Repo(prg1,"log13.txt");
            ctr13 = new Controller(repo1, false);
        }
        catch (Exception ex) {
            err += "Program 13: " + ex.getMessage() + "\n";
        }
         */

        //ex14
        IStmt declA = new VarDeclStmt("a", new IntType());
        IStmt declB = new VarDeclStmt("b", new IntType());
        IStmt declC = new VarDeclStmt("c", new IntType());
        IStmt assignA = new AssignStmt("a", new ValExp(new IntValue(1)));
        IStmt assignB = new AssignStmt("b", new ValExp(new IntValue(2)));
        IStmt assignC = new AssignStmt("c", new ValExp(new IntValue(5)));
        IStmt case1 = new CompStmt(new PrintStmt(new VarExp("a")), new PrintStmt(new VarExp("b")));
        IStmt case2 = new CompStmt(new PrintStmt(new ValExp(new IntValue(100))), new PrintStmt(new ValExp(new IntValue(200))));
        IStmt defaultS = new PrintStmt(new ValExp(new IntValue(300)));
        Exp switchExp = new ArithExp('*', new VarExp("a"), new ValExp(new IntValue(10)));
        Exp case1Exp = new ArithExp('*', new VarExp("b"), new VarExp("c"));
        Exp case2Exp = new ValExp(new IntValue(10));
        IStmt switchS = new SwitchStmt(switchExp, case1Exp, case1, case2Exp, case2, defaultS);

        IStmt ex14 = new CompStmt(declA,
                    new CompStmt(declB,
                    new CompStmt(declC,
                    new CompStmt(assignA,
                    new CompStmt(assignB,
                    new CompStmt(assignC,
                    new CompStmt(switchS,
                            new PrintStmt(new ValExp(new IntValue(300))))))))));
        ex14.typecheck(new MyDictionary<String, Type>());
        PrgState prg14 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex14);
        IRepo repo14 = new Repo(prg14,"log14.txt");
        ctr14 = new Controller(repo14, false);

        //ex15
        IStmt declV = new VarDeclStmt("v1", new RefType(new IntType()));
        IStmt decCnt = new VarDeclStmt("cnt", new IntType());
        IStmt allocV = new HeapAllocStmt("v1", new ValExp(new IntValue(1)));
        IStmt createSem = new CreateSemaphoreStmt("cnt", new HeapReadExp(new VarExp("v1")));
        IStmt mulV10 = new HeapWriteStmt("v1", new ArithExp('*', new HeapReadExp(new VarExp("v1")), new ValExp(new IntValue(10))));
        IStmt printV = new PrintStmt(new HeapReadExp(new VarExp("v1")));
        IStmt fork1 = new ForkStmt(new CompStmt(new AcquireStmt("cnt"), new CompStmt(mulV10, new CompStmt(printV, new ReleaseStmt("cnt")))));
        IStmt mulV2 = new HeapWriteStmt("v1", new ArithExp('*', new HeapReadExp(new VarExp("v1")), new ValExp(new IntValue(2))));
        IStmt fork2 = new ForkStmt(new CompStmt(new AcquireStmt("cnt"), new CompStmt(mulV10, new CompStmt(mulV2, new CompStmt(printV.deepCopy(), new ReleaseStmt("cnt"))))));
        IStmt printV1 = new PrintStmt(new ArithExp('-', new HeapReadExp(new VarExp("v1")), new ValExp(new IntValue(1))));

        IStmt ex15 = new CompStmt(declV,
                    new CompStmt(decCnt,
                    new CompStmt(allocV,
                    new CompStmt(createSem,
                    new CompStmt(fork1,
                    new CompStmt(fork2,
                    new CompStmt(new AcquireStmt("cnt"),
                    new CompStmt(printV1,
                            new ReleaseStmt("cnt")))))))));
        ex15.typecheck(new MyDictionary<String, Type>());
        PrgState prg15 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(), new MyDictionary<StringValue, BufferedReader>(), new Heap<Value>(), new SemaphoreTable(), ex15);
        IRepo repo15 = new Repo(prg15,"log15.txt");
        ctr15 = new Controller(repo15, false);

        if (err != "") {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Toy Language - Typecheck Error");
            alert.setHeaderText(err);
            alert.setContentText("Press ok to continue");
            alert.showAndWait();
        }

        List<Controller> lst = new ArrayList<>();
        lst.add(ctr1);
        lst.add(ctr2);
        lst.add(ctr3);
        lst.add(ctr4);
        lst.add(ctr5);
        lst.add(ctr6);
        lst.add(ctr7);
        lst.add(ctr8);
        lst.add(ctr9);
        lst.add(ctr10);
        lst.add(ctr11);
        lst.add(ctr12);
        lst.add(ctr13);
        lst.add(ctr14);
        lst.add(ctr15);

        lst = lst.stream().filter(x -> x != null).toList();

        ObservableList<Controller> prgList = FXCollections.observableArrayList();

        prgList.addAll(lst);

        ProgramList.setItems(prgList);
        ProgramList.getSelectionModel().selectFirst();
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        setUp();
    }

    @FXML
    protected void onLaunch() throws Exception{
        Controller selectedProgram = ProgramList.getSelectionModel().getSelectedItem();

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("program-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1062, 563);
        ProgramViewController prgView = fxmlLoader.getController();
        prgView.setController(selectedProgram);
        prgView.setUp();
        Stage stage = new Stage();
        stage.setTitle("Program running");
        stage.setScene(scene);
        stage.show();
    }
}