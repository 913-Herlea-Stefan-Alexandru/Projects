/********************************************************************************
** Form generated from reading UI file 'lmdbgui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LMDBGUI_H
#define UI_LMDBGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LMDBGUIClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *LMDBGUIClass)
    {
        if (LMDBGUIClass->objectName().isEmpty())
            LMDBGUIClass->setObjectName(QString::fromUtf8("LMDBGUIClass"));
        LMDBGUIClass->resize(600, 400);
        menuBar = new QMenuBar(LMDBGUIClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        LMDBGUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(LMDBGUIClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        LMDBGUIClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(LMDBGUIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        LMDBGUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(LMDBGUIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        LMDBGUIClass->setStatusBar(statusBar);

        retranslateUi(LMDBGUIClass);

        QMetaObject::connectSlotsByName(LMDBGUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *LMDBGUIClass)
    {
        LMDBGUIClass->setWindowTitle(QCoreApplication::translate("LMDBGUIClass", "LMDBGUI", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LMDBGUIClass: public Ui_LMDBGUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LMDBGUI_H
