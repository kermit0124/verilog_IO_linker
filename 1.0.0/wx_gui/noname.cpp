///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MainFrame::MainFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer19;
	bSizer19 = new wxBoxSizer( wxHORIZONTAL );

	wxStaticBoxSizer* sbSizer2;
	sbSizer2 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Source port") ), wxVERTICAL );

	wxStaticBoxSizer* sbSizer9;
	sbSizer9 = new wxStaticBoxSizer( new wxStaticBox( sbSizer2->GetStaticBox(), wxID_ANY, wxT("Configuration") ), wxVERTICAL );

	m_comboBox__src_inst_filter = new wxComboBox( sbSizer9->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer9->Add( m_comboBox__src_inst_filter, 0, wxALL|wxEXPAND, 5 );


	sbSizer2->Add( sbSizer9, 0, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer5;
	sbSizer5 = new wxStaticBoxSizer( new wxStaticBox( sbSizer2->GetStaticBox(), wxID_ANY, wxT("Pins") ), wxVERTICAL );

	m_listBox__src = new wxListBox( sbSizer5->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_HSCROLL|wxLB_MULTIPLE );
	sbSizer5->Add( m_listBox__src, 1, wxALL|wxALIGN_CENTER_VERTICAL|wxEXPAND, 5 );


	sbSizer2->Add( sbSizer5, 1, wxEXPAND, 5 );

	m_button__output_tracer = new wxButton( sbSizer2->GetStaticBox(), wxID_ANY, wxT("Tracer link"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer2->Add( m_button__output_tracer, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer19->Add( sbSizer2, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer22;
	bSizer22 = new wxBoxSizer( wxVERTICAL );


	bSizer22->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__connect = new wxButton( this, wxID_ANY, wxT(">> Connect >>"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer22->Add( m_button__connect, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticline5 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer22->Add( m_staticline5, 0, wxEXPAND | wxALL, 5 );

	wxStaticBoxSizer* sbSizer8;
	sbSizer8 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Modify assign mode") ), wxVERTICAL );

	m_staticText7 = new wxStaticText( sbSizer8->GetStaticBox(), wxID_ANY, wxT("Wire name"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText7->Wrap( -1 );
	sbSizer8->Add( m_staticText7, 0, wxALL, 5 );

	m_textCtrl__agnModeName = new wxTextCtrl( sbSizer8->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer8->Add( m_textCtrl__agnModeName, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticText6 = new wxStaticText( sbSizer8->GetStaticBox(), wxID_ANY, wxT("Assign segment"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	sbSizer8->Add( m_staticText6, 0, wxALL, 5 );

	m_textCtrl__agnModeSeg = new wxTextCtrl( sbSizer8->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer8->Add( m_textCtrl__agnModeSeg, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxEXPAND, 5 );

	m_staticText5 = new wxStaticText( sbSizer8->GetStaticBox(), wxID_ANY, wxT("Verilog:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText5->Wrap( -1 );
	sbSizer8->Add( m_staticText5, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_button__assign = new wxButton( sbSizer8->GetStaticBox(), wxID_ANY, wxT("Assign"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer8->Add( m_button__assign, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticline6 = new wxStaticLine( sbSizer8->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	sbSizer8->Add( m_staticline6, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer33;
	bSizer33 = new wxBoxSizer( wxHORIZONTAL );

	m_textCtrl__createWireName = new wxTextCtrl( sbSizer8->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer33->Add( m_textCtrl__createWireName, 1, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	wxString m_choice__create_wireIO_typeChoices[] = { wxT("input"), wxT("output"), wxT("inout"), wxT("wire") };
	int m_choice__create_wireIO_typeNChoices = sizeof( m_choice__create_wireIO_typeChoices ) / sizeof( wxString );
	m_choice__create_wireIO_type = new wxChoice( sbSizer8->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice__create_wireIO_typeNChoices, m_choice__create_wireIO_typeChoices, 0 );
	m_choice__create_wireIO_type->SetSelection( 0 );
	bSizer33->Add( m_choice__create_wireIO_type, 0, wxALL, 5 );


	sbSizer8->Add( bSizer33, 1, wxEXPAND, 5 );

	m_textCtrl__createWireSeg = new wxTextCtrl( sbSizer8->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer8->Add( m_textCtrl__createWireSeg, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxEXPAND, 5 );

	m_button__create_wireIO = new wxButton( sbSizer8->GetStaticBox(), wxID_ANY, wxT("Create wire/IO"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer8->Add( m_button__create_wireIO, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer22->Add( sbSizer8, 1, wxEXPAND, 5 );


	bSizer22->Add( 0, 0, 1, wxEXPAND, 5 );


	bSizer19->Add( bSizer22, 1, wxEXPAND|wxALIGN_CENTER_VERTICAL, 5 );

	wxStaticBoxSizer* sbSizer4;
	sbSizer4 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Destination port") ), wxVERTICAL );

	wxStaticBoxSizer* sbSizer10;
	sbSizer10 = new wxStaticBoxSizer( new wxStaticBox( sbSizer4->GetStaticBox(), wxID_ANY, wxT("Configuration") ), wxHORIZONTAL );

	m_comboBox__dest_inst_filter = new wxComboBox( sbSizer10->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer10->Add( m_comboBox__dest_inst_filter, 1, wxALL, 5 );

	m_checkBox7 = new wxCheckBox( sbSizer10->GetStaticBox(), wxID_ANY, wxT("Ignore assigned pin"), wxDefaultPosition, wxDefaultSize, 0 );
	m_checkBox7->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_BTNTEXT ) );
	m_checkBox7->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	sbSizer10->Add( m_checkBox7, 0, wxALL, 5 );


	sbSizer4->Add( sbSizer10, 0, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer51;
	sbSizer51 = new wxStaticBoxSizer( new wxStaticBox( sbSizer4->GetStaticBox(), wxID_ANY, wxT("Pins") ), wxVERTICAL );

	m_listBox__dest = new wxListBox( sbSizer51->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_HSCROLL|wxLB_MULTIPLE );
	sbSizer51->Add( m_listBox__dest, 1, wxALL|wxALIGN_CENTER_VERTICAL|wxEXPAND, 5 );


	sbSizer4->Add( sbSizer51, 1, wxEXPAND, 5 );

	m_button__destDisconnect = new wxButton( sbSizer4->GetStaticBox(), wxID_ANY, wxT("Disconnect"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer4->Add( m_button__destDisconnect, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer19->Add( sbSizer4, 1, wxEXPAND, 5 );


	bSizer2->Add( bSizer19, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer2 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	m_menu2 = new wxMenu();
	wxMenuItem* m_menuItem11;
	m_menuItem11 = new wxMenuItem( m_menu2, wxID_ANY, wxString( wxT("Module manager") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu2->Append( m_menuItem11 );

	m_menubar1->Append( m_menu2, wxT("File") );

	m_menu21 = new wxMenu();
	wxMenuItem* m_menuItem1;
	m_menuItem1 = new wxMenuItem( m_menu21, wxID_ANY, wxString( wxT("Replace bit width by wrapper parameter") ) , wxEmptyString, wxITEM_CHECK );
	m_menu21->Append( m_menuItem1 );
	m_menuItem1->Enable( false );

	m_menubar1->Append( m_menu21, wxT("View") );

	this->SetMenuBar( m_menubar1 );


	this->Centre( wxBOTH );

	// Connect Events
	this->Connect( wxEVT_ACTIVATE, wxActivateEventHandler( MainFrame::mainFrame__onAct ) );
	m_listBox__src->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::src__onListBox ), NULL, this );
	m_button__connect->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::connect__onBtnClick ), NULL, this );
	m_button__assign->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::assign__onBtnClick ), NULL, this );
	m_button__create_wireIO->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::create_wireIO__onBtnClick ), NULL, this );
	m_listBox__dest->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::dest__onListBox ), NULL, this );
	m_button__destDisconnect->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::destDisconnect__onBtnClick ), NULL, this );
	m_menu2->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::menu_moduleManager__onMenuSel ), this, m_menuItem11->GetId());
}

MainFrame::~MainFrame()
{
	// Disconnect Events
	this->Disconnect( wxEVT_ACTIVATE, wxActivateEventHandler( MainFrame::mainFrame__onAct ) );
	m_listBox__src->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::src__onListBox ), NULL, this );
	m_button__connect->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::connect__onBtnClick ), NULL, this );
	m_button__assign->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::assign__onBtnClick ), NULL, this );
	m_button__create_wireIO->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::create_wireIO__onBtnClick ), NULL, this );
	m_listBox__dest->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::dest__onListBox ), NULL, this );
	m_button__destDisconnect->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::destDisconnect__onBtnClick ), NULL, this );

}

VerilogCodeFrame::VerilogCodeFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer15;
	bSizer15 = new wxBoxSizer( wxVERTICAL );

	m_richText__showGen = new wxRichTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0|wxVSCROLL|wxHSCROLL|wxNO_BORDER|wxWANTS_CHARS );
	bSizer15->Add( m_richText__showGen, 1, wxEXPAND | wxALL, 5 );


	this->SetSizer( bSizer15 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	this->Connect( wxEVT_ACTIVATE, wxActivateEventHandler( VerilogCodeFrame::VerilogCodeFrame__onAct ) );
}

VerilogCodeFrame::~VerilogCodeFrame()
{
	// Disconnect Events
	this->Disconnect( wxEVT_ACTIVATE, wxActivateEventHandler( VerilogCodeFrame::VerilogCodeFrame__onAct ) );

}

ModuleManagerFrame::ModuleManagerFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* bSizer23;
	bSizer23 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer24;
	bSizer24 = new wxBoxSizer( wxHORIZONTAL );

	m_filePicker__loadFile = new wxFilePickerCtrl( this, wxID_ANY, wxT("D:\\dev\\py3\\verilog_IO_linker\\1.0.0\\wx_gui\\noname.h"), wxT("Select a file"), wxT("*.*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer24->Add( m_filePicker__loadFile, 1, wxALL|wxEXPAND, 5 );


	bSizer23->Add( bSizer24, 0, wxEXPAND, 5 );

	m_staticline5 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer23->Add( m_staticline5, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer241;
	bSizer241 = new wxBoxSizer( wxHORIZONTAL );

	m_listBox__parser_module = new wxListBox( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizer241->Add( m_listBox__parser_module, 1, wxALL|wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer13;
	sbSizer13 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Configuration") ), wxVERTICAL );

	wxBoxSizer* bSizer28;
	bSizer28 = new wxBoxSizer( wxVERTICAL );


	bSizer28->Add( 0, 0, 1, wxEXPAND, 5 );

	m_staticText39 = new wxStaticText( sbSizer13->GetStaticBox(), wxID_ANY, wxT("Instance name"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText39->Wrap( -1 );
	bSizer28->Add( m_staticText39, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl__inst_name = new wxTextCtrl( sbSizer13->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer28->Add( m_textCtrl__inst_name, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL|wxEXPAND, 5 );

	m_button__inst = new wxButton( sbSizer13->GetStaticBox(), wxID_ANY, wxT("Instance"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer28->Add( m_button__inst, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticline3 = new wxStaticLine( sbSizer13->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer28->Add( m_staticline3, 0, wxEXPAND | wxALL, 5 );


	bSizer28->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__set_wrapper = new wxButton( sbSizer13->GetStaticBox(), wxID_ANY, wxT("Set wrapper"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer28->Add( m_button__set_wrapper, 1, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_staticline81 = new wxStaticLine( sbSizer13->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer28->Add( m_staticline81, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer26;
	bSizer26 = new wxBoxSizer( wxHORIZONTAL );

	m_button__createNewWrapper = new wxButton( sbSizer13->GetStaticBox(), wxID_ANY, wxT("Create new wrapper"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer26->Add( m_button__createNewWrapper, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl__createNewWrapper = new wxTextCtrl( sbSizer13->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer26->Add( m_textCtrl__createNewWrapper, 1, wxALL, 5 );


	bSizer28->Add( bSizer26, 1, wxEXPAND, 5 );


	sbSizer13->Add( bSizer28, 1, wxEXPAND, 5 );


	bSizer241->Add( sbSizer13, 1, wxEXPAND, 5 );

	m_listBox__inst = new wxListBox( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizer241->Add( m_listBox__inst, 1, wxALL|wxEXPAND, 5 );


	bSizer23->Add( bSizer241, 1, wxEXPAND, 5 );

	m_staticline51 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer23->Add( m_staticline51, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer30;
	bSizer30 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* bSizer31;
	bSizer31 = new wxBoxSizer( wxVERTICAL );

	m_staticText411 = new wxStaticText( this, wxID_ANY, wxT("Overrider parameters"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText411->Wrap( -1 );
	bSizer31->Add( m_staticText411, 0, wxALL, 5 );

	m_listBox__override_param = new wxListBox( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizer31->Add( m_listBox__override_param, 1, wxALL|wxEXPAND, 5 );


	bSizer30->Add( bSizer31, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer32;
	bSizer32 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer35;
	bSizer35 = new wxBoxSizer( wxVERTICAL );


	bSizer35->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__param_mapping = new wxButton( this, wxID_ANY, wxT("Mapping ->>"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer35->Add( m_button__param_mapping, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticline4 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer35->Add( m_staticline4, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer36;
	bSizer36 = new wxBoxSizer( wxHORIZONTAL );

	m_button__overrideParamByConst = new wxButton( this, wxID_ANY, wxT("<<- Set constant"), wxDefaultPosition, wxDefaultSize, 0 );
	m_button__overrideParamByConst->Hide();

	bSizer36->Add( m_button__overrideParamByConst, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl3 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl3->Hide();

	bSizer36->Add( m_textCtrl3, 1, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );


	bSizer35->Add( bSizer36, 1, wxEXPAND, 5 );


	bSizer35->Add( 0, 0, 1, wxEXPAND, 5 );


	bSizer32->Add( bSizer35, 1, wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer30->Add( bSizer32, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer33;
	bSizer33 = new wxBoxSizer( wxVERTICAL );

	m_staticText4111 = new wxStaticText( this, wxID_ANY, wxT("Wrapper parameters"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4111->Wrap( -1 );
	bSizer33->Add( m_staticText4111, 0, wxALL, 5 );

	m_listBox__wrapper_param = new wxListBox( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizer33->Add( m_listBox__wrapper_param, 1, wxALL|wxEXPAND, 5 );

	wxBoxSizer* bSizer34;
	bSizer34 = new wxBoxSizer( wxHORIZONTAL );

	m_button__createNewParam = new wxButton( this, wxID_ANY, wxT("Add"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer34->Add( m_button__createNewParam, 1, wxALL, 5 );

	m_button__del_wrapper_param = new wxButton( this, wxID_ANY, wxT("Delete"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer34->Add( m_button__del_wrapper_param, 1, wxALL, 5 );


	bSizer33->Add( bSizer34, 0, wxEXPAND, 5 );

	wxBoxSizer* bSizer20;
	bSizer20 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* bSizer21;
	bSizer21 = new wxBoxSizer( wxVERTICAL );

	m_staticText19 = new wxStaticText( this, wxID_ANY, wxT("name"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText19->Wrap( -1 );
	bSizer21->Add( m_staticText19, 0, wxALL, 5 );

	m_staticText20 = new wxStaticText( this, wxID_ANY, wxT("value"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText20->Wrap( -1 );
	bSizer21->Add( m_staticText20, 0, wxALL, 5 );


	bSizer20->Add( bSizer21, 0, wxEXPAND, 5 );

	wxBoxSizer* bSizer211;
	bSizer211 = new wxBoxSizer( wxVERTICAL );

	m_textCtrl__newParam_name = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer211->Add( m_textCtrl__newParam_name, 0, wxALL|wxEXPAND, 5 );

	m_textCtrl_newParam_value = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer211->Add( m_textCtrl_newParam_value, 0, wxALL|wxEXPAND, 5 );


	bSizer20->Add( bSizer211, 1, wxEXPAND, 5 );


	bSizer33->Add( bSizer20, 0, wxEXPAND, 5 );


	bSizer30->Add( bSizer33, 1, wxEXPAND, 5 );


	bSizer23->Add( bSizer30, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer23 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_filePicker__loadFile->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( ModuleManagerFrame::filePicker__onFileChanged ), NULL, this );
	m_listBox__parser_module->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::parser_module__onListBox ), NULL, this );
	m_button__inst->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::inst__onButtonClick ), NULL, this );
	m_button__set_wrapper->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::loadAsWrapper__onBtnClick ), NULL, this );
	m_button__createNewWrapper->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewWrapper__onBtnClick ), NULL, this );
	m_listBox__inst->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::inst__onListBox ), NULL, this );
	m_button__param_mapping->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::mapping__onBtnClick ), NULL, this );
	m_button__overrideParamByConst->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::overrideParamByConst__onBtnClick ), NULL, this );
	m_button__createNewParam->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewParam__onBtnClick ), NULL, this );
}

ModuleManagerFrame::~ModuleManagerFrame()
{
	// Disconnect Events
	m_filePicker__loadFile->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( ModuleManagerFrame::filePicker__onFileChanged ), NULL, this );
	m_listBox__parser_module->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::parser_module__onListBox ), NULL, this );
	m_button__inst->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::inst__onButtonClick ), NULL, this );
	m_button__set_wrapper->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::loadAsWrapper__onBtnClick ), NULL, this );
	m_button__createNewWrapper->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewWrapper__onBtnClick ), NULL, this );
	m_listBox__inst->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::inst__onListBox ), NULL, this );
	m_button__param_mapping->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::mapping__onBtnClick ), NULL, this );
	m_button__overrideParamByConst->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::overrideParamByConst__onBtnClick ), NULL, this );
	m_button__createNewParam->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewParam__onBtnClick ), NULL, this );

}
