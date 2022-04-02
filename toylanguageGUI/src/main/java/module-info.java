module controllers.toylanguagegui {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;

    opens controllers.toylanguagegui to javafx.fxml;
    opens model.adt to javafx.base;
    exports controllers.toylanguagegui;
}