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

	wxBoxSizer* bSizer68;
	bSizer68 = new wxBoxSizer( wxVERTICAL );

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

	m_listBox__src = new wxListBox( sbSizer5->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_HSCROLL );
	sbSizer5->Add( m_listBox__src, 1, wxALL|wxALIGN_CENTER_VERTICAL|wxEXPAND, 5 );


	sbSizer2->Add( sbSizer5, 1, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer44;
	sbSizer44 = new wxStaticBoxSizer( new wxStaticBox( sbSizer2->GetStaticBox(), wxID_ANY, wxT("Detials") ), wxVERTICAL );

	m_notebook7 = new wxNotebook( sbSizer44->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxNB_BOTTOM );
	m_notebook7->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	m_panel3 = new wxPanel( m_notebook7, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer70;
	bSizer70 = new wxBoxSizer( wxVERTICAL );

	m_textCtrl__src_info = new wxTextCtrl( m_panel3, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_DONTWRAP|wxTE_MULTILINE );
	m_textCtrl__src_info->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	bSizer70->Add( m_textCtrl__src_info, 1, wxALL|wxEXPAND, 5 );


	m_panel3->SetSizer( bSizer70 );
	m_panel3->Layout();
	bSizer70->Fit( m_panel3 );
	m_notebook7->AddPage( m_panel3, wxT("Information"), true );
	m_panel4 = new wxPanel( m_notebook7, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer71;
	bSizer71 = new wxBoxSizer( wxVERTICAL );

	m_listBox__src_linkTo = new wxListBox( m_panel4, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizer71->Add( m_listBox__src_linkTo, 1, wxALL|wxEXPAND, 5 );


	m_panel4->SetSizer( bSizer71 );
	m_panel4->Layout();
	bSizer71->Fit( m_panel4 );
	m_notebook7->AddPage( m_panel4, wxT("Link to"), false );

	sbSizer44->Add( m_notebook7, 1, wxEXPAND | wxALL, 5 );


	sbSizer2->Add( sbSizer44, 1, wxEXPAND, 5 );

	m_button__output_tracer = new wxButton( sbSizer2->GetStaticBox(), wxID_ANY, wxT("Tracer link"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer2->Add( m_button__output_tracer, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer19->Add( sbSizer2, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer24;
	bSizer24 = new wxBoxSizer( wxVERTICAL );


	bSizer24->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__connect = new wxButton( this, wxID_ANY, wxT("Link\n>--->"), wxDefaultPosition, wxDefaultSize, 0 );
	m_button__connect->SetMaxSize( wxSize( 70,-1 ) );

	bSizer24->Add( m_button__connect, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer24->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__codeWin = new wxButton( this, wxID_ANY, wxT("Code\nwindow"), wxDefaultPosition, wxDefaultSize, 0 );
	m_button__codeWin->SetMaxSize( wxSize( 70,-1 ) );

	bSizer24->Add( m_button__codeWin, 0, wxALL, 5 );


	bSizer19->Add( bSizer24, 0, wxEXPAND, 5 );

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

	wxStaticBoxSizer* sbSizer441;
	sbSizer441 = new wxStaticBoxSizer( new wxStaticBox( sbSizer4->GetStaticBox(), wxID_ANY, wxT("Detials") ), wxVERTICAL );

	m_notebook71 = new wxNotebook( sbSizer441->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxNB_BOTTOM );
	m_notebook71->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	m_panel31 = new wxPanel( m_notebook71, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer701;
	bSizer701 = new wxBoxSizer( wxVERTICAL );

	m_textCtrl__dest_info = new wxTextCtrl( m_panel31, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_DONTWRAP|wxTE_MULTILINE );
	bSizer701->Add( m_textCtrl__dest_info, 1, wxALL|wxEXPAND, 5 );


	m_panel31->SetSizer( bSizer701 );
	m_panel31->Layout();
	bSizer701->Fit( m_panel31 );
	m_notebook71->AddPage( m_panel31, wxT("Information"), false );

	sbSizer441->Add( m_notebook71, 1, wxEXPAND | wxALL, 5 );


	sbSizer4->Add( sbSizer441, 1, wxEXPAND, 5 );

	m_button__destDisconnect = new wxButton( sbSizer4->GetStaticBox(), wxID_ANY, wxT("Disconnect"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer4->Add( m_button__destDisconnect, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer19->Add( sbSizer4, 1, wxEXPAND, 5 );


	bSizer68->Add( bSizer19, 1, wxEXPAND, 5 );


	bSizer2->Add( bSizer68, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer2 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	m_menu2 = new wxMenu();
	wxMenuItem* m_menuItem11;
	m_menuItem11 = new wxMenuItem( m_menu2, wxID_ANY, wxString( wxT("Module manager") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu2->Append( m_menuItem11 );

	m_menubar1->Append( m_menu2, wxT("Window") );

	m_menu21 = new wxMenu();
	wxMenuItem* m_menuItem1;
	m_menuItem1 = new wxMenuItem( m_menu21, wxID_ANY, wxString( wxT("Replace bit width by wrapper parameter") ) , wxEmptyString, wxITEM_CHECK );
	m_menu21->Append( m_menuItem1 );
	m_menuItem1->Enable( false );

	m_menubar1->Append( m_menu21, wxT("View") );

	m_menu5 = new wxMenu();
	wxMenuItem* m_menuItem4;
	m_menuItem4 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("Add a point") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem4 );

	m_menubar1->Append( m_menu5, wxT("Edit") );

	m_menu4 = new wxMenu();
	wxMenuItem* m_menuItem__multSel;
	m_menuItem__multSel = new wxMenuItem( m_menu4, wxID_ANY, wxString( wxT("Destination multiple selection") ) , wxEmptyString, wxITEM_CHECK );
	m_menu4->Append( m_menuItem__multSel );

	wxMenuItem* m_menuItem__autoNext;
	m_menuItem__autoNext = new wxMenuItem( m_menu4, wxID_ANY, wxString( wxT("Auto select to next after link") ) , wxEmptyString, wxITEM_CHECK );
	m_menu4->Append( m_menuItem__autoNext );
	m_menuItem__autoNext->Check( true );

	m_menubar1->Append( m_menu4, wxT("Mode") );

	this->SetMenuBar( m_menubar1 );


	this->Centre( wxBOTH );

	// Connect Events
	this->Connect( wxEVT_ACTIVATE, wxActivateEventHandler( MainFrame::mainFrame__onAct ) );
	m_listBox__src->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::src__onListBox ), NULL, this );
	m_button__connect->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::connect__onBtnClick ), NULL, this );
	m_button__codeWin->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::codeWin__onBtnClick ), NULL, this );
	m_listBox__dest->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::dest__onListBox ), NULL, this );
	m_button__destDisconnect->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::destDisconnect__onBtnClick ), NULL, this );
	m_menu2->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::menu_moduleManager__onMenuSel ), this, m_menuItem11->GetId());
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::menu_addPoint__onMenuSel ), this, m_menuItem4->GetId());
	m_menu4->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::menu_addPoint__destMultSel ), this, m_menuItem__multSel->GetId());
	m_menu4->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::menu_addPoint__autoSel ), this, m_menuItem__autoNext->GetId());
}

MainFrame::~MainFrame()
{
	// Disconnect Events
	this->Disconnect( wxEVT_ACTIVATE, wxActivateEventHandler( MainFrame::mainFrame__onAct ) );
	m_listBox__src->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::src__onListBox ), NULL, this );
	m_button__connect->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::connect__onBtnClick ), NULL, this );
	m_button__codeWin->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::codeWin__onBtnClick ), NULL, this );
	m_listBox__dest->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::dest__onListBox ), NULL, this );
	m_button__destDisconnect->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::destDisconnect__onBtnClick ), NULL, this );

}

CreatePointDialog::CreatePointDialog( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* bSizer44;
	bSizer44 = new wxBoxSizer( wxVERTICAL );

	wxFlexGridSizer* fgSizer4;
	fgSizer4 = new wxFlexGridSizer( 0, 2, 0, 0 );
	fgSizer4->SetFlexibleDirection( wxBOTH );
	fgSizer4->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	wxString m_choice__create_point_typeChoices[] = { wxT("input"), wxT("output"), wxT("inout"), wxT("wire") };
	int m_choice__create_point_typeNChoices = sizeof( m_choice__create_point_typeChoices ) / sizeof( wxString );
	m_choice__create_point_type = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice__create_point_typeNChoices, m_choice__create_point_typeChoices, 0 );
	m_choice__create_point_type->SetSelection( 0 );
	fgSizer4->Add( m_choice__create_point_type, 0, wxALL, 5 );

	m_textCtrl__point_name = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl__point_name->SetMinSize( wxSize( 300,-1 ) );

	fgSizer4->Add( m_textCtrl__point_name, 1, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticText144 = new wxStaticText( this, wxID_ANY, wxT("Bit width"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText144->Wrap( -1 );
	fgSizer4->Add( m_staticText144, 0, wxALL, 5 );

	m_textCtrl__point_bit = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl__point_bit->SetMinSize( wxSize( 300,-1 ) );

	fgSizer4->Add( m_textCtrl__point_bit, 1, wxALL, 5 );

	m_staticText140 = new wxStaticText( this, wxID_ANY, wxT("Wire assign code"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText140->Wrap( -1 );
	fgSizer4->Add( m_staticText140, 0, wxALL, 5 );

	m_textCtrl__wire_assign_code = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl__wire_assign_code->Enable( false );
	m_textCtrl__wire_assign_code->SetMinSize( wxSize( 300,-1 ) );

	fgSizer4->Add( m_textCtrl__wire_assign_code, 1, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer44->Add( fgSizer4, 1, wxEXPAND, 5 );

	m_staticline8 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer44->Add( m_staticline8, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer45;
	bSizer45 = new wxBoxSizer( wxHORIZONTAL );

	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("Point info."), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer45->Add( m_staticText1, 0, wxALL, 5 );

	m_staticText__pointInfo = new wxStaticText( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText__pointInfo->Wrap( -1 );
	bSizer45->Add( m_staticText__pointInfo, 0, wxALL, 5 );


	bSizer44->Add( bSizer45, 0, wxEXPAND, 5 );

	m_button__create_point = new wxButton( this, wxID_ANY, wxT("Create wire/IO to wrapper"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer44->Add( m_button__create_point, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	this->SetSizer( bSizer44 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_choice__create_point_type->Connect( wxEVT_COMMAND_CHOICE_SELECTED, wxCommandEventHandler( CreatePointDialog::point_type__onChoice ), NULL, this );
	m_textCtrl__point_name->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::point_name__onText ), NULL, this );
	m_textCtrl__point_bit->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::point_bit__onText ), NULL, this );
	m_textCtrl__wire_assign_code->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::wire_assign_code__onText ), NULL, this );
	m_button__create_point->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( CreatePointDialog::create_point__onBtnClick ), NULL, this );
}

CreatePointDialog::~CreatePointDialog()
{
	// Disconnect Events
	m_choice__create_point_type->Disconnect( wxEVT_COMMAND_CHOICE_SELECTED, wxCommandEventHandler( CreatePointDialog::point_type__onChoice ), NULL, this );
	m_textCtrl__point_name->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::point_name__onText ), NULL, this );
	m_textCtrl__point_bit->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::point_bit__onText ), NULL, this );
	m_textCtrl__wire_assign_code->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( CreatePointDialog::wire_assign_code__onText ), NULL, this );
	m_button__create_point->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( CreatePointDialog::create_point__onBtnClick ), NULL, this );

}

VerilogCodeFrame::VerilogCodeFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* bSizer15;
	bSizer15 = new wxBoxSizer( wxVERTICAL );

	wxStaticBoxSizer* sbSizer16;
	sbSizer16 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Generate code") ), wxVERTICAL );

	m_richText__showGen = new wxRichTextCtrl( sbSizer16->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0|wxVSCROLL|wxHSCROLL|wxNO_BORDER|wxWANTS_CHARS );
	m_richText__showGen->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INFOBK ) );

	sbSizer16->Add( m_richText__showGen, 1, wxEXPAND | wxALL, 5 );


	bSizer15->Add( sbSizer16, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer26;
	bSizer26 = new wxBoxSizer( wxHORIZONTAL );

	wxStaticBoxSizer* sbSizer14;
	sbSizer14 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("File directory") ), wxVERTICAL );

	m_dirPicker1 = new wxDirPickerCtrl( sbSizer14->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a folder"), wxDefaultPosition, wxDefaultSize, wxDIRP_DEFAULT_STYLE );
	sbSizer14->Add( m_dirPicker1, 1, wxALL|wxEXPAND, 5 );


	bSizer26->Add( sbSizer14, 1, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer15;
	sbSizer15 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("File name(.v)") ), wxVERTICAL );

	wxBoxSizer* bSizer27;
	bSizer27 = new wxBoxSizer( wxHORIZONTAL );

	m_textCtrl__fileName = new wxTextCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl__fileName->SetMinSize( wxSize( 150,-1 ) );

	bSizer27->Add( m_textCtrl__fileName, 0, wxALL, 5 );

	m_button__genFile = new wxButton( sbSizer15->GetStaticBox(), wxID_ANY, wxT("Generate file"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer27->Add( m_button__genFile, 0, wxALL, 5 );


	sbSizer15->Add( bSizer27, 1, wxEXPAND, 5 );


	bSizer26->Add( sbSizer15, 0, wxEXPAND, 5 );


	bSizer15->Add( bSizer26, 0, wxEXPAND, 5 );


	this->SetSizer( bSizer15 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	this->Connect( wxEVT_ACTIVATE, wxActivateEventHandler( VerilogCodeFrame::VerilogCodeFrame__onAct ) );
	this->Connect( wxEVT_CLOSE_WINDOW, wxCloseEventHandler( VerilogCodeFrame::VerilogCodeFrame__onClose ) );
	m_button__genFile->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( VerilogCodeFrame::genFile__onBtnClick ), NULL, this );
}

VerilogCodeFrame::~VerilogCodeFrame()
{
	// Disconnect Events
	this->Disconnect( wxEVT_ACTIVATE, wxActivateEventHandler( VerilogCodeFrame::VerilogCodeFrame__onAct ) );
	this->Disconnect( wxEVT_CLOSE_WINDOW, wxCloseEventHandler( VerilogCodeFrame::VerilogCodeFrame__onClose ) );
	m_button__genFile->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( VerilogCodeFrame::genFile__onBtnClick ), NULL, this );

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

	wxStaticBoxSizer* sbSizer10;
	sbSizer10 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Module list") ), wxVERTICAL );

	m_listBox__parser_module = new wxListBox( sbSizer10->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer10->Add( m_listBox__parser_module, 1, wxALL|wxEXPAND, 5 );


	bSizer241->Add( sbSizer10, 1, wxEXPAND, 5 );

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

	wxStaticBoxSizer* sbSizer11;
	sbSizer11 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Instance list") ), wxVERTICAL );

	m_listBox__inst = new wxListBox( sbSizer11->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer11->Add( m_listBox__inst, 1, wxALL|wxEXPAND, 5 );


	bSizer241->Add( sbSizer11, 1, wxEXPAND, 5 );


	bSizer23->Add( bSizer241, 1, wxEXPAND, 5 );

	m_staticline51 = new wxStaticLine( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL );
	bSizer23->Add( m_staticline51, 0, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer30;
	bSizer30 = new wxBoxSizer( wxHORIZONTAL );

	wxStaticBoxSizer* sbSizer12;
	sbSizer12 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Instance parameters") ), wxVERTICAL );

	m_listBox__override_param = new wxListBox( sbSizer12->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer12->Add( m_listBox__override_param, 1, wxALL|wxEXPAND, 5 );

	m_button12 = new wxButton( sbSizer12->GetStaticBox(), wxID_ANY, wxT("Clear override"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer12->Add( m_button12, 0, wxALL|wxEXPAND, 5 );

	wxBoxSizer* bSizer25;
	bSizer25 = new wxBoxSizer( wxHORIZONTAL );

	m_button__overrideParamByConst = new wxButton( sbSizer12->GetStaticBox(), wxID_ANY, wxT("Set constant"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer25->Add( m_button__overrideParamByConst, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl__setInstParamByConst = new wxTextCtrl( sbSizer12->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer25->Add( m_textCtrl__setInstParamByConst, 1, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );


	sbSizer12->Add( bSizer25, 0, wxEXPAND, 5 );


	bSizer30->Add( sbSizer12, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer32;
	bSizer32 = new wxBoxSizer( wxVERTICAL );


	bSizer32->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__param_mapping = new wxButton( this, wxID_ANY, wxT("<<-- Override --<"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer32->Add( m_button__param_mapping, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	bSizer32->Add( 0, 0, 1, wxEXPAND, 5 );


	bSizer30->Add( bSizer32, 1, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer131;
	sbSizer131 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Wrapper parameters") ), wxVERTICAL );

	m_listBox__wrapper_param = new wxListBox( sbSizer131->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	sbSizer131->Add( m_listBox__wrapper_param, 1, wxALL|wxEXPAND, 5 );

	wxBoxSizer* bSizer34;
	bSizer34 = new wxBoxSizer( wxHORIZONTAL );

	m_button__createNewParam = new wxButton( sbSizer131->GetStaticBox(), wxID_ANY, wxT("Add"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer34->Add( m_button__createNewParam, 1, wxALL, 5 );

	m_button__del_wrapper_param = new wxButton( sbSizer131->GetStaticBox(), wxID_ANY, wxT("Delete"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer34->Add( m_button__del_wrapper_param, 1, wxALL, 5 );


	sbSizer131->Add( bSizer34, 0, wxEXPAND, 5 );

	wxBoxSizer* bSizer20;
	bSizer20 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* bSizer21;
	bSizer21 = new wxBoxSizer( wxVERTICAL );

	m_staticText19 = new wxStaticText( sbSizer131->GetStaticBox(), wxID_ANY, wxT("name"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText19->Wrap( -1 );
	bSizer21->Add( m_staticText19, 0, wxALL, 5 );

	m_staticText20 = new wxStaticText( sbSizer131->GetStaticBox(), wxID_ANY, wxT("value"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText20->Wrap( -1 );
	bSizer21->Add( m_staticText20, 0, wxALL, 5 );


	bSizer20->Add( bSizer21, 0, wxEXPAND, 5 );

	wxBoxSizer* bSizer211;
	bSizer211 = new wxBoxSizer( wxVERTICAL );

	m_textCtrl__newParam_name = new wxTextCtrl( sbSizer131->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer211->Add( m_textCtrl__newParam_name, 0, wxALL|wxEXPAND, 5 );

	m_textCtrl_newParam_value = new wxTextCtrl( sbSizer131->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer211->Add( m_textCtrl_newParam_value, 0, wxALL|wxEXPAND, 5 );


	bSizer20->Add( bSizer211, 1, wxEXPAND, 5 );


	sbSizer131->Add( bSizer20, 0, wxEXPAND, 5 );


	bSizer30->Add( sbSizer131, 1, wxEXPAND, 5 );


	bSizer23->Add( bSizer30, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer23 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	this->Connect( wxEVT_CLOSE_WINDOW, wxCloseEventHandler( ModuleManagerFrame::moduleManagerFrame__onClose ) );
	m_filePicker__loadFile->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( ModuleManagerFrame::filePicker__onFileChanged ), NULL, this );
	m_listBox__parser_module->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::parser_module__onListBox ), NULL, this );
	m_button__inst->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::inst__onButtonClick ), NULL, this );
	m_button__set_wrapper->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::loadAsWrapper__onBtnClick ), NULL, this );
	m_button__createNewWrapper->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewWrapper__onBtnClick ), NULL, this );
	m_listBox__inst->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::inst__onListBox ), NULL, this );
	m_button12->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::clearInstParamOverride__onBtnClick ), NULL, this );
	m_button__overrideParamByConst->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::overrideParamByConst__onBtnClick ), NULL, this );
	m_button__param_mapping->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::mapping__onBtnClick ), NULL, this );
	m_button__createNewParam->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewParam__onBtnClick ), NULL, this );
	m_button__del_wrapper_param->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::delWrapParam__onBtnClick ), NULL, this );
}

ModuleManagerFrame::~ModuleManagerFrame()
{
	// Disconnect Events
	this->Disconnect( wxEVT_CLOSE_WINDOW, wxCloseEventHandler( ModuleManagerFrame::moduleManagerFrame__onClose ) );
	m_filePicker__loadFile->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( ModuleManagerFrame::filePicker__onFileChanged ), NULL, this );
	m_listBox__parser_module->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::parser_module__onListBox ), NULL, this );
	m_button__inst->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::inst__onButtonClick ), NULL, this );
	m_button__set_wrapper->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::loadAsWrapper__onBtnClick ), NULL, this );
	m_button__createNewWrapper->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewWrapper__onBtnClick ), NULL, this );
	m_listBox__inst->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( ModuleManagerFrame::inst__onListBox ), NULL, this );
	m_button12->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::clearInstParamOverride__onBtnClick ), NULL, this );
	m_button__overrideParamByConst->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::overrideParamByConst__onBtnClick ), NULL, this );
	m_button__param_mapping->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::mapping__onBtnClick ), NULL, this );
	m_button__createNewParam->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::createNewParam__onBtnClick ), NULL, this );
	m_button__del_wrapper_param->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModuleManagerFrame::delWrapParam__onBtnClick ), NULL, this );

}
