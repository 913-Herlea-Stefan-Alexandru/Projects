#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_lmdbgui.h"

class LMDBGUI : public QMainWindow
{
    Q_OBJECT

public:
    LMDBGUI(QWidget *parent = Q_NULLPTR);

private:
    Ui::LMDBGUIClass ui;
};
