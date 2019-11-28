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
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/choice.h>
#include <wx/sizer.h>
#include <wx/textctrl.h>
#include <wx/checkbox.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/richtext/richtextctrl.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class Frame1
///////////////////////////////////////////////////////////////////////////////
class Frame1 : public wxFrame
{
	private:

	protected:
		wxStaticText* m_staticText19;
		wxChoice* m_choice__modSel;
		wxStaticText* m_staticText15;
		wxTextCtrl* m_textCtrl__instName;
		wxStaticText* m_staticText16;
		wxTextCtrl* m_textCtrl__prefix;
		wxStaticText* m_staticText171;
		wxTextCtrl* m_textCtrl__suffix;
		wxStaticText* m_staticText18;
		wxChoice* m_choice__left_comma;
		wxStaticText* m_staticText6;
		wxCheckBox* m_checkBox__gen_agn_in;
		wxCheckBox* m_checkBox__gen_agn_out;
		wxStaticText* m_staticText7;
		wxCheckBox* m_checkBox__wire_mode;
		wxStaticText* m_staticText8;
		wxChoice* m_choice__para_mapping_mode;
		wxButton* m_button64;
		wxRichTextCtrl* m_richText__origSrc;
		wxButton* m_button__genCode;
		wxRichTextCtrl* m_richText__genSrc;

		// Virtual event handlers, overide them in your derived class
		virtual void OnChoice__moduleSel( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnKeyUp__all_txtCtrl( wxKeyEvent& event ) { event.Skip(); }
		virtual void onText__instName( wxCommandEvent& event ) { event.Skip(); }
		virtual void rtxt_origSrc__onText( wxCommandEvent& event ) { event.Skip(); }
		virtual void gen_code( wxCommandEvent& event ) { event.Skip(); }


	public:

		Frame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("verilog IO linker"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1346,677 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~Frame1();

};

