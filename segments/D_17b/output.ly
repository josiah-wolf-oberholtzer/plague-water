\version "2.19.1"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/plague-water-header.ly"
\include "../../stylesheets/plague-water-layout.ly"
\include "../../stylesheets/plague-water-paper.ly"

#(set-default-paper-size "11x17" 'landscape)
#(set-global-staff-size 14)

\score {
	\context Score = "Plague Water Score" \with {
		\override HorizontalBracket #'color = #red
	} <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box 17B }
				\tempo 4=96
				\time 7/8
				s1 * 7/8
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 7/8
				s1 * 7/8
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				s1 * 3/16
			}
			{
				\time 5/8
				s1 * 5/8
			}
			{
				\time 7/8
				s1 * 7/8
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 7/8
				s1 * 7/8
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 7/8
				s1 * 7/8
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				s1 * 3/16
			}
		}
		\context SaxophoneStaffGroup = "Saxophone Staff Group" <<
			\context SaxophoneStaff = "Saxophone Staff" {
				\clef "percussion"
				\context Voice = "Saxophone Voice" {
					{
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							c'4 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 1
							c'16 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 2
							b'16 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							b'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							c'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							c'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'4
						}
						{
							\set stemLeftBeamCount = -1
							\set stemRightBeamCount = 1
							f'8 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							f'8
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							ef'8 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							ef'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							c'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							d'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							bf'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							bf'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							bf'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							bf'8
						}
						{
							d'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							b'8.
						}
						{
							af'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							d'8 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							d'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							cs'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							cs'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							e'8. [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 1
							e'16
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 2
							e'16 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							e'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							e'8 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							cs'8
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							cs'8.
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							cs'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
					}
				}
			}
		>>
		\context GuitarStaffGroup = "Guitar Staff Group" <<
			\context GuitarStaff = "Guitar Staff" {
				\clef "percussion"
				\context Voice = "Guitar Voice" {
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 7/8
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							c'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							b'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							d'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							d'8 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							d'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							d'8 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							bf'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							b'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							b'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							bf'8 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							d'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r8.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							bf'8 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							bf'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							b'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r2
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 7/16
							\stopStaff
							\startStaff
						}
						{
							r4.
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
					}
				}
			}
			\context Dynamics = "Guitar Pedals" {
			}
		>>
		\context PianoStaffGroup = "Piano Staff Group" <<
			\context PianoUpperStaff = "Piano Upper Staff" <<
				\clef "treble"
				\context Voice = "Piano RH Voice" {
					{
						{
							r4
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							ef'16 ~
							ef'4 ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							ef'8 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							ef'8
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							d'8. ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							c'4 ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							c'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							f'2
						}
						{
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 0
							af'8
						}
						{
							b'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							af'4
						}
						{
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							af'8. [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							d'8. ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							d'8 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							d'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'4
						}
						{
							e'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8.
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							cs'16 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = -1
							cs'8 ]
						}
						{
							cs'4
						}
						{
							\set stemLeftBeamCount = -1
							\set stemRightBeamCount = 1
							cs'8 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							cs'8
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							e'8 ] ~
							e'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
				}
			>>
			\context Dynamics = "Piano Dynamics" {
			}
			\context PianoLowerStaff = "Piano Lower Staff" <<
				\clef "bass"
				\context Voice = "Piano LH Voice" {
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							d'4 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							d'16
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							b'8
						}
						{
							ef'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r4
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							f'8.
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							b'4. ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 1
							b'16 [
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 2
							b'16 ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 1
							b'8
						}
						{
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							d'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							b'8 ~
							b'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8.
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							d'8
						}
						{
							af'4.
						}
						{
							e'4 ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							cs'8 ~
							cs'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							cs'16 ~
							cs'4 ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							cs'16
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8.
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
				}
			>>
			\context Dynamics = "Piano Pedals" {
			}
		>>
		\context PercussionStaffGroup = "Percussion Staff Group" <<
			\context PercussionShakerStaff = "Percussion Shaker Staff" {
				\clef "percussion"
				\context Voice = "Percussion RH Voice" {
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							f'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							f'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							cs'8 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							cs'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r2
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							af'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							af'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							af'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
							r4
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							bf'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 7/16
							\stopStaff
							\startStaff
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							bf'8.
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r4
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							cs'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8.
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
					}
				}
			}
			\context PercussionDrumStaff = "Percussion Drum Staff" {
				\clef "percussion"
				\context Voice = "Percussion LH Voice" {
					{
						{
							r4.
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							cs'8 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							cs'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							d'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							d'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
							r4
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							b'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							b'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							ef'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							af'4
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4.
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							d'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							b'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							r8.
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							b'16 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							b'8 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
							r16
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 2
							af'16 [ ~
							\set stemLeftBeamCount = 2
							\set stemRightBeamCount = 0
							af'16 ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r8.
							r4
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 7/16
							\stopStaff
							\startStaff
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							e'8
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r4
							r8
						}
					}
					{
						{
							\override Stem.stemlet-length = 0.75
							\set stemLeftBeamCount = 0
							\set stemRightBeamCount = 1
							cs'8 [ ~
							\set stemLeftBeamCount = 1
							\set stemRightBeamCount = 0
							cs'8. ]
							\revert Stem.stemlet-length
						}
					}
					{
						{
							r16
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
							\stopStaff
							\startStaff
						}
						{
							\stopStaff
							\once \override Staff.StaffSymbol.line-count = 1
							\startStaff
							R1 * 3/16
								_ \markup {
									\italic
										\right-column
											{
												" "
												" "
												" "
												"Jamaica Plain"
												"December 2013 - February 2014"
											}
									}
							\stopStaff
							\startStaff
							\bar "|."
						}
					}
				}
			}
		>>
	>>
}