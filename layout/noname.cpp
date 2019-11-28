///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

Frame1::Frame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer10;
	bSizer10 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer13;
	bSizer13 = new wxBoxSizer( wxVERTICAL );

	m_staticText19 = new wxStaticText( this, wxID_ANY, wxT("Module select"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText19->Wrap( -1 );
	bSizer13->Add( m_staticText19, 0, wxALL, 5 );

	wxArrayString m_choice__modSelChoices;
	m_choice__modSel = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice__modSelChoices, 0 );
	m_choice__modSel->SetSelection( 0 );
	m_choice__modSel->SetMinSize( wxSize( 300,-1 ) );

	bSizer13->Add( m_choice__modSel, 0, wxALL, 5 );


	bSizer10->Add( bSizer13, 1, wxEXPAND, 5 );

	wxGridSizer* gSizer4;
	gSizer4 = new wxGridSizer( 0, 2, 0, 0 );

	gSizer4->SetMinSize( wxSize( -1,400 ) );
	m_staticText15 = new wxStaticText( this, wxID_ANY, wxT("Instance name"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText15->Wrap( -1 );
	gSizer4->Add( m_staticText15, 0, wxALL, 5 );

	m_textCtrl__instName = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer4->Add( m_textCtrl__instName, 0, wxALL, 5 );

	m_staticText16 = new wxStaticText( this, wxID_ANY, wxT("Prefix"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText16->Wrap( -1 );
	gSizer4->Add( m_staticText16, 0, wxALL, 5 );

	m_textCtrl__prefix = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer4->Add( m_textCtrl__prefix, 0, wxALL, 5 );

	m_staticText171 = new wxStaticText( this, wxID_ANY, wxT("Suffix"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText171->Wrap( -1 );
	gSizer4->Add( m_staticText171, 0, wxALL, 5 );

	m_textCtrl__suffix = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer4->Add( m_textCtrl__suffix, 0, wxALL, 5 );

	m_staticText18 = new wxStaticText( this, wxID_ANY, wxT("Left comma mode"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText18->Wrap( -1 );
	gSizer4->Add( m_staticText18, 0, wxALL, 5 );

	wxString m_choice__left_commaChoices[] = { wxT("false"), wxT("true") };
	int m_choice__left_commaNChoices = sizeof( m_choice__left_commaChoices ) / sizeof( wxString );
	m_choice__left_comma = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice__left_commaNChoices, m_choice__left_commaChoices, 0 );
	m_choice__left_comma->SetSelection( 0 );
	gSizer4->Add( m_choice__left_comma, 0, wxALL, 5 );

	m_staticText6 = new wxStaticText( this, wxID_ANY, wxT("Generate assign"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	gSizer4->Add( m_staticText6, 0, wxALL, 5 );

	wxBoxSizer* bSizer81;
	bSizer81 = new wxBoxSizer( wxVERTICAL );

	m_checkBox__gen_agn_in = new wxCheckBox( this, wxID_ANY, wxT("input/inout"), wxDefaultPosition, wxDefaultSize, 0 );
	m_checkBox__gen_agn_in->SetValue(true);
	bSizer81->Add( m_checkBox__gen_agn_in, 0, wxALL, 5 );

	m_checkBox__gen_agn_out = new wxCheckBox( this, wxID_ANY, wxT("output"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer81->Add( m_checkBox__gen_agn_out, 0, wxALL, 5 );


	gSizer4->Add( bSizer81, 1, wxEXPAND, 5 );

	m_staticText7 = new wxStaticText( this, wxID_ANY, wxT("Wire prefix add \"_\""), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText7->Wrap( -1 );
	gSizer4->Add( m_staticText7, 0, wxALL, 5 );

	m_checkBox__wire_mode = new wxCheckBox( this, wxID_ANY, wxT("enable"), wxDefaultPosition, wxDefaultSize, 0 );
	m_checkBox__wire_mode->SetValue(true);
	gSizer4->Add( m_checkBox__wire_mode, 0, wxALL, 5 );

	m_staticText8 = new wxStaticText( this, wxID_ANY, wxT("Localpara mapping mode"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText8->Wrap( -1 );
	gSizer4->Add( m_staticText8, 0, wxALL, 5 );

	wxString m_choice__para_mapping_modeChoices[] = { wxT("value"), wxT("name") };
	int m_choice__para_mapping_modeNChoices = sizeof( m_choice__para_mapping_modeChoices ) / sizeof( wxString );
	m_choice__para_mapping_mode = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice__para_mapping_modeNChoices, m_choice__para_mapping_modeChoices, 0 );
	m_choice__para_mapping_mode->SetSelection( 1 );
	gSizer4->Add( m_choice__para_mapping_mode, 0, wxALL, 5 );


	bSizer10->Add( gSizer4, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer15;
	bSizer15 = new wxBoxSizer( wxVERTICAL );

	m_button64 = new wxButton( this, wxID_ANY, wxT("Load source code"), wxDefaultPosition, wxDefaultSize, 0 );
	m_button64->Enable( false );

	bSizer15->Add( m_button64, 0, wxALL, 5 );


	bSizer10->Add( bSizer15, 1, wxEXPAND, 5 );


	bSizer8->Add( bSizer10, 1, wxEXPAND, 5 );


	bSizer7->Add( bSizer8, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer9;
	bSizer9 = new wxBoxSizer( wxHORIZONTAL );

	m_richText__origSrc = new wxRichTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0|wxALWAYS_SHOW_SB|wxHSCROLL|wxVSCROLL );
	m_richText__origSrc->SetMinSize( wxSize( 450,500 ) );

	bSizer9->Add( m_richText__origSrc, 1, wxEXPAND | wxALL, 5 );

	wxBoxSizer* bSizer16;
	bSizer16 = new wxBoxSizer( wxVERTICAL );


	bSizer16->Add( 0, 0, 1, wxEXPAND, 5 );

	m_button__genCode = new wxButton( this, wxID_ANY, wxT("Generate\n>>>"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer16->Add( m_button__genCode, 0, wxALL, 5 );


	bSizer16->Add( 0, 0, 1, wxEXPAND, 5 );


	bSizer9->Add( bSizer16, 1, wxEXPAND, 5 );

	m_richText__genSrc = new wxRichTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0|wxALWAYS_SHOW_SB|wxHSCROLL|wxVSCROLL );
	m_richText__genSrc->SetMinSize( wxSize( 450,500 ) );

	bSizer9->Add( m_richText__genSrc, 1, wxEXPAND | wxALL, 5 );


	bSizer7->Add( bSizer9, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer7 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_choice__modSel->Connect( wxEVT_COMMAND_CHOICE_SELECTED, wxCommandEventHandler( Frame1::OnChoice__moduleSel ), NULL, this );
	m_choice__modSel->Connect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__instName->Connect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__instName->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Frame1::onText__instName ), NULL, this );
	m_textCtrl__prefix->Connect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__suffix->Connect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_choice__left_comma->Connect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_richText__origSrc->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Frame1::rtxt_origSrc__onText ), NULL, this );
	m_button__genCode->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( Frame1::gen_code ), NULL, this );
}

Frame1::~Frame1()
{
	// Disconnect Events
	m_choice__modSel->Disconnect( wxEVT_COMMAND_CHOICE_SELECTED, wxCommandEventHandler( Frame1::OnChoice__moduleSel ), NULL, this );
	m_choice__modSel->Disconnect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__instName->Disconnect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__instName->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Frame1::onText__instName ), NULL, this );
	m_textCtrl__prefix->Disconnect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_textCtrl__suffix->Disconnect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_choice__left_comma->Disconnect( wxEVT_KEY_UP, wxKeyEventHandler( Frame1::OnKeyUp__all_txtCtrl ), NULL, this );
	m_richText__origSrc->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Frame1::rtxt_origSrc__onText ), NULL, this );
	m_button__genCode->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( Frame1::gen_code ), NULL, this );

}
