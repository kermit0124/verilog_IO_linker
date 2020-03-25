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
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/statline.h>
#include <wx/stattext.h>
#include <wx/textctrl.h>
#include <wx/choice.h>
#include <wx/checkbox.h>
#include <wx/menu.h>
#include <wx/frame.h>
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
		wxButton* m_button__output_tracer;
		wxButton* m_button__connect;
		wxStaticLine* m_staticline5;
		wxStaticText* m_staticText7;
		wxTextCtrl* m_textCtrl__agnModeName;
		wxStaticText* m_staticText6;
		wxTextCtrl* m_textCtrl__agnModeSeg;
		wxStaticText* m_staticText5;
		wxButton* m_button__assign;
		wxStaticLine* m_staticline6;
		wxTextCtrl* m_textCtrl__createWireName;
		wxChoice* m_choice__create_wireIO_type;
		wxTextCtrl* m_textCtrl__createWireSeg;
		wxButton* m_button__create_wireIO;
		wxComboBox* m_comboBox__dest_inst_filter;
		wxCheckBox* m_checkBox7;
		wxListBox* m_listBox__dest;
		wxButton* m_button__disconnect_input;
		wxMenuBar* m_menubar1;
		wxMenu* m_menu2;
		wxMenu* m_menu21;

		// Virtual event handlers, overide them in your derived class
		virtual void mainFrame__onAct( wxActivateEvent& event ) { event.Skip(); }
		virtual void src__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void connect__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void assign__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void create_wireIO__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void dest__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void menu_moduleManager__onMenuSel( wxCommandEvent& event ) { event.Skip(); }


	public:

		MainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 983,624 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MainFrame();

};

///////////////////////////////////////////////////////////////////////////////
/// Class VerilogCodeFrame
///////////////////////////////////////////////////////////////////////////////
class VerilogCodeFrame : public wxFrame
{
	private:

	protected:
		wxRichTextCtrl* m_richText__showGen;

		// Virtual event handlers, overide them in your derived class
		virtual void VerilogCodeFrame__onAct( wxActivateEvent& event ) { event.Skip(); }


	public:

		VerilogCodeFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 909,669 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

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
		wxStaticText* m_staticText411;
		wxListBox* m_listBox__override_param;
		wxButton* m_button__param_mapping;
		wxStaticLine* m_staticline4;
		wxButton* m_button__overrideParamByConst;
		wxTextCtrl* m_textCtrl3;
		wxStaticText* m_staticText4111;
		wxListBox* m_listBox__wrapper_param;
		wxButton* m_button__createNewParam;
		wxButton* m_button__del_wrapper_param;
		wxStaticText* m_staticText19;
		wxStaticText* m_staticText20;
		wxTextCtrl* m_textCtrl__newParam_name;
		wxTextCtrl* m_textCtrl_newParam_value;

		// Virtual event handlers, overide them in your derived class
		virtual void filePicker__onFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void parser_module__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void inst__onButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void loadAsWrapper__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void createNewWrapper__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void inst__onListBox( wxCommandEvent& event ) { event.Skip(); }
		virtual void mapping__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void overrideParamByConst__onBtnClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void createNewParam__onBtnClick( wxCommandEvent& event ) { event.Skip(); }


	public:

		ModuleManagerFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1250,765 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~ModuleManagerFrame();

};

