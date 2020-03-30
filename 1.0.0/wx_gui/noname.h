///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/combobox.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/sizer.h>
#include <wx/statbox.h>
#include <wx/listbox.h>
#include <wx/textctrl.h>
#include <wx/panel.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/notebook.h>
#include <wx/button.h>
#include <wx/checkbox.h>
#include <wx/menu.h>
#include <wx/frame.h>
#include <wx/choice.h>
#include <wx/stattext.h>
#include <wx/statline.h>
#include <wx/dialog.h>
#include <wx/richtext/richtextctrl.h>
#include <wx/filepicker.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MainFrame
///////////////////////////////////////////////////////////////////////////////
class MainFrame : public wxFrame
{
	private:

	protected:
		wxComboBox* m_comboBox__src_inst_filter;
		wxListBox* m_listBox__src;
		wxNotebook* m_notebook7;
		wxPanel* m_panel3;
		wxTextCtrl* m_textCtrl__src_info;
		wxPanel* m_panel4;
		wxListBox* m_listBox__src_linkTo;
		wxButton* m_button__output_tracer;
		wxButton* m_button__connect;
		wxButton* m_button__codeWin;
		wxComboBox* m_comboBox__dest_inst_filter;
		wxCheckBox* m_checkBox7;
		wxListBox* m_listBox__dest;
		wxNotebook* m_notebook71;
		wxPanel* m_panel31;
		wxTextCtrl* m_textCtrl__dest_info;
		wxButton* m_button__destDisconnect;
		wxMenuBar* m_menubar1;
		wxMenu* m_menu2;
		wxMenu* m_menu21;
		wxMenu* m_menu5;
		wxMenu* m_menu4;

		// Virtual event handlers, overide them in your derived class
		virtual void mainFrame__onAct( wxActivateEvent& event ) { event.Skip(); }
		virtual void src__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void connect__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void codeWin__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void dest__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void destDisconnect__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void menu_moduleManager__onMenuSel( wxCommandEvent& event ) { event.Skip(); }
		virtual void menu_addPoint__onMenuSel( wxCommandEvent& event ) { event.Skip(); }
		virtual void menu_addPoint__destMultSel( wxCommandEvent& event ) { event.Skip(); }
		virtual void menu_addPoint__autoSel( wxCommandEvent& event ) { event.Skip(); }


	public:

		MainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1096,684 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MainFrame();

};

///////////////////////////////////////////////////////////////////////////////
/// Class CreatePointDialog
///////////////////////////////////////////////////////////////////////////////
class CreatePointDialog : public wxDialog
{
	private:

	protected:
		wxChoice* m_choice__create_point_type;
		wxTextCtrl* m_textCtrl__point_name;
		wxStaticText* m_staticText144;
		wxTextCtrl* m_textCtrl__point_bit;
		wxStaticText* m_staticText140;
		wxTextCtrl* m_textCtrl__wire_assign_code;
		wxStaticLine* m_staticline8;
		wxStaticText* m_staticText1;
		wxStaticText* m_staticText__pointInfo;
		wxButton* m_button__create_point;

		// Virtual event handlers, overide them in your derived class
		virtual void point_type__onChoice( wxCommandEvent& event ) { event.Skip(); }
		virtual void point_name__onText( wxCommandEvent& event ) { event.Skip(); }
		virtual void point_bit__onText( wxCommandEvent& event ) { event.Skip(); }
		virtual void wire_assign_code__onText( wxCommandEvent& event ) { event.Skip(); }
		virtual void create_point__onBtnClick( wxCommandEvent& event ) { event.Skip(); }


	public:

		CreatePointDialog( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Create point"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 477,220 ), long style = wxDEFAULT_DIALOG_STYLE );
		~CreatePointDialog();

};

///////////////////////////////////////////////////////////////////////////////
/// Class VerilogCodeFrame
///////////////////////////////////////////////////////////////////////////////
class VerilogCodeFrame : public wxFrame
{
	private:

	protected:
		wxRichTextCtrl* m_richText__showGen;
		wxDirPickerCtrl* m_dirPicker1;
		wxTextCtrl* m_textCtrl__fileName;
		wxButton* m_button__genFile;

		// Virtual event handlers, overide them in your derived class
		virtual void VerilogCodeFrame__onAct( wxActivateEvent& event ) { event.Skip(); }
		virtual void VerilogCodeFrame__onClose( wxCloseEvent& event ) { event.Skip(); }
		virtual void genFile__onBtnClick( wxCommandEvent& event ) { event.Skip(); }


	public:

		VerilogCodeFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Verilog Code Generator"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 909,669 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~VerilogCodeFrame();

};

///////////////////////////////////////////////////////////////////////////////
/// Class ModuleManagerFrame
///////////////////////////////////////////////////////////////////////////////
class ModuleManagerFrame : public wxFrame
{
	private:

	protected:
		wxFilePickerCtrl* m_filePicker__loadFile;
		wxStaticLine* m_staticline5;
		wxListBox* m_listBox__parser_module;
		wxStaticText* m_staticText39;
		wxTextCtrl* m_textCtrl__inst_name;
		wxButton* m_button__inst;
		wxStaticLine* m_staticline3;
		wxButton* m_button__set_wrapper;
		wxStaticLine* m_staticline81;
		wxButton* m_button__createNewWrapper;
		wxTextCtrl* m_textCtrl__createNewWrapper;
		wxListBox* m_listBox__inst;
		wxStaticLine* m_staticline51;
		wxListBox* m_listBox__override_param;
		wxButton* m_button12;
		wxButton* m_button__overrideParamByConst;
		wxTextCtrl* m_textCtrl__setInstParamByConst;
		wxButton* m_button__param_mapping;
		wxListBox* m_listBox__wrapper_param;
		wxButton* m_button__createNewParam;
		wxButton* m_button__del_wrapper_param;
		wxStaticText* m_staticText19;
		wxStaticText* m_staticText20;
		wxTextCtrl* m_textCtrl__newParam_name;
		wxTextCtrl* m_textCtrl_newParam_value;

		// Virtual event handlers, overide them in your derived class
		virtual void moduleManagerFrame__onClose( wxCloseEvent& event ) { event.Skip(); }
		virtual void filePicker__onFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void parser_module__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void inst__onButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void loadAsWrapper__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void createNewWrapper__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void inst__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void clearInstParamOverride__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void overrideParamByConst__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void mapping__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void createNewParam__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void delWrapParam__onBtnClick( wxCommandEvent& event ) { event.Skip(); }


	public:

		ModuleManagerFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Module Manager"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 974,760 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~ModuleManagerFrame();

};

