%
% Book design for Git in the Trenches
%

\NeedsTeXFormat{LaTeX2e}[1994/06/01]

\ProvidesClass{gitt}[2011/05/15 v1.0.0 GITT book design]

% The 'screen' option creates a PDF suitable for reading on a computer screen
% The 'print' option creates a PDF suitable for printing
\providecommand{\gitt@format}{screen}% default format
\DeclareOption{screen}{\gdef\gitt@format{screen}}
\DeclareOption{print}{\gdef\gitt@format{print}}


% All other options are passed along to the base class
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{book}%
}
\ProcessOptions*\relax


\LoadClass[openright,12pt]{book}

% set paper size
%\setstocksize{24.59cm}{18.90cm}
%%\settrims{1.91cm}{0cm}
%\settrimmedsize{\stockheight}{\stockwidth}{*}
%\setlrmarginsandblock{2.79cm}{2.29cm}{*}
%\setulmarginsandblock{2.91cm}{2.91cm}{*}
%%\setmarginnotes{0.5cm}{2cm}{0.2cm}
%\checkandfixthelayout

\RequirePackage[paperheight=24.59cm,paperwidth=18.90cm,headheight=\baselineskip,textheight=35\baselineskip]{geometry}

% Reset the figure numbering at the beginning of each chapter and print only
% the figure number (not including the chapter number).
\renewcommand{\thefigure}{\arabic{figure}}

% Import packages
\RequirePackage{xifthen}
\RequirePackage{graphicx}
\RequirePackage{color,fancyvrb,relsize}
\RequirePackage{tikz}
\RequirePackage{makeidx}
\RequirePackage{eso-pic}
\PassOptionsToPackage{usenames,dvipsnames,svgnames}{xcolor}
\makeindex


% Import a new font and use the sans-serif version by default
%\RequirePackage{lmodern}
%\renewcommand{\familydefault}{\sfdefault}

% Font settings
\RequirePackage{fontspec}
\setmainfont[Mapping=tex-text,Numbers=OldStyle]{Linux Libertine O}

% Small caps
\newcommand{\smallcaps}[1]{%
  {\addfontfeature{LetterSpace=5.0}\textsc{\MakeTextLowercase{#1}}}%
}

% Running heads and feet
\RequirePackage{textcase}
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\thepage\quad\smallcaps{\leftmark}}
\fancyhead[RO]{\smallcaps{\rightmark}\quad\thepage}
\renewcommand{\headrulewidth}{0pt}

% Front matter
\renewcommand\frontmatter{%
  \cleardoublepage%
  \@mainmatterfalse%
  \pagenumbering{roman}%
  \fancyhf{}%
  \renewcommand{\chaptermark}[1]{\markboth{##1}{}}%
  \renewcommand{\sectionmark}[1]{\markright{##1}}%
  \fancyhead[LE]{\thepage\quad\smallcaps{\leftmark}}% chapter title
  \fancyhead[RO]{\smallcaps{\rightmark}\quad\thepage}% section title
}

% Main matter
\renewcommand\mainmatter{%
  \cleardoublepage%
  \@mainmattertrue%
  \pagenumbering{arabic}%
  \fancyhf{}%
  \renewcommand{\chaptermark}[1]{\markboth{##1}{}}%
  \renewcommand{\sectionmark}[1]{\markright{##1}}%
  \fancyhead[LE]{\thepage\quad\smallcaps{\leftmark}}% chapter title
  \fancyhead[RO]{\smallcaps{\rightmark}\quad\thepage}% section title
}




% When cleardoublepage is called, produce a blank (empty) page -- i.e.,
% without headers and footers
\def\cleardoublepage{%
  \clearpage
  \if@twoside%
    \ifodd\c@page\else
      \hbox{}%
      %\vspace*{\fill}
      %\begin{center}
      %  This page intentionally contains only this sentence.
      %\end{center}
      %\vspace{\fill}
      \thispagestyle{empty}%
      \newpage%
      \if@twocolumn\hbox{}\newpage\fi%
    \fi%
  \fi%
}




% Put chapters and sections in the toc, only number the chapter
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{0}

% Make chapter names disappear
\renewcommand{\chaptername}{}
\renewcommand{\thechapter}{}
\renewcommand{\tablename}{}
\renewcommand{\thetable}{}

% Print just the chapter name without 'Chapter #.' in the running heads
%\renewcommand\chaptermark[1]{\markboth{\memUChead{#1}}{}}%

% Make the pdf have clickable links
\RequirePackage[
  bookmarks,
  bookmarksopen,
  bookmarksnumbered=false,
  colorlinks,
  pdfpagemode=None,
  urlcolor=black,
  citecolor=black,
  linkcolor=black,
  plainpages=false,
  pdfpagelabels,
  pdftitle={Git in the Trenches},
  pdfauthor={Peter Savage}]{hyperref}

\AtBeginDocument{
  \hyphenpenalty=1000
  \tolerance=1000
}

% give us a begin{trenches}
\newenvironment{trenches}{\begin{quote}\begin{rmfamily}\textbf{In the trenches\ldots\\\\}}{\end{rmfamily}\end{quote}}

% Callout boxes
\newsavebox{\callout@contents}
\newcommand{\callout@type}{}
\newcommand{\callout@title}{}
\newenvironment{callout}[2]{%
  \xdef\callout@type{#1}% typeset in a box along the left
  \xdef\callout@title{#2}% typeset in a box along the top
  \begin{lrbox}{\callout@contents}%
    \begin{minipage}{.9\textwidth}%
}{%
    \end{minipage}%
  \end{lrbox}%
  \begin{figure}[hbt]%
    \tikzstyle{mybox} = [draw=black, fill=gray!20, very thick, rectangle, rounded corners, inner sep=15pt, inner ysep=20pt]
    \tikzstyle{fancytitle} = [fill=black, text=white]
    \hskip-10pt% allows the type block to hang into the left margin
    \begin{tikzpicture}%
      \node[mybox] (box) {\usebox{\callout@contents}};
      \node[fancytitle, right=16pt] at (box.north west) {\callout@title};
      \node[fancytitle, rounded corners] at (box.west) {\rotatebox{90}{\callout@type}};
    \end{tikzpicture}%
  \end{figure}%
}

% Indicates thought breaks
\newcommand{\thoughtbreak}{%
  \par\begin{center}*\quad*\quad*\end{center}\par
}

% Clear page commands from memoir.cls
\newcommand{\cleartoevenpage}[1][\@empty]{%
  \clearpage%
  \ifodd\c@page\hbox{}#1\clearpage\fi%
}

\newcommand{\cleartooddpage}[1][\@empty]{%
  \clearpage%
  \ifodd\c@page\else\hbox{}#1\clearpage\fi%
}


% Inserts full-page graphics for cover pages.
\newcommand{\coverpage}[1]{%
  \thispagestyle{empty}%
  \IfFileExists{#1}{%
    \AddToShipoutPicture*{\put(0,0){\includegraphics[width=\paperwidth,height=\paperheight]{#1}}}%
  }{%
    \ClassWarningNoLine{gitt}{Missing cover page graphic:\MessageBreak #1}%
  }%
}

\newcommand{\frontcover}[1]{%
  \ifthenelse{\equal{\gitt@format}{screen}}{%
    \coverpage{#1}%
    \null\cleardoublepage
  }{%
    \ClassWarningNoLine{gitt}{Ignoring \string\frontcover because we're not generating a screen format.}%
  }%
}

\newcommand{\backcover}[1]{%
  \ifthenelse{\equal{\gitt@format}{screen}}{%
    \cleartoevenpage[\thispagestyle{empty}]%
    \coverpage{#1}%
    \null%
  }{%
    \ClassWarningNoLine{gitt}{Ignoring \string\backcover because we're not generating a screen format.}%
  }%
}

\newcommand{\indexref}[1]{%
\index{#1|textit}%
}

\newcommand{\indexcom}[2]{%
\index{#1@\texttt{#2}}
}

\newcommand{\indexgit}[1]{%
\texttt{git #1}%
\index{git commands!#1@\texttt{#1}}%
}

\RequirePackage{listings}
\RequirePackage{courier}
\lstnewenvironment{code}{
  \lstset{
    basicstyle=\tiny\ttfamily,
    identifierstyle=\tiny\ttfamily,
    commentstyle=\tiny\ttfamily,
    stringstyle=\tiny\ttfamily,
    keywordstyle=\tiny\bfseries\ttfamily,
    frame=leftline,
    framerule=1mm,
    framextopmargin=0pt,
    framexbottommargin=0pt,
    framexleftmargin=2pt,
    framexrightmargin=2pt,
    xleftmargin=8pt,
    xrightmargin=2pt,
    breaklines=true,
    breakatwhitespace=true,
    breakindent=4pt,
    postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\hookrightarrow}},
    tabsize=2,
    showstringspaces=false,
    aboveskip=14pt,
    belowskip=14pt,
    morecomment=[l][\tiny\bfseries\ttfamily]{john@satsuki:},
    morecomment=[l][\tiny\bfseries\ttfamily]{rob@mimi:}
    %moredelim=[is][\tiny\bfseries\ttfamily]{|||}{|||}
  }
}{}

% Table of contents
\renewcommand\tableofcontents{%
  \if@twocolumn
    \@restonecoltrue\onecolumn
  \else
    \@restonecolfalse
  \fi
  \chapter*{\contentsname
    \@mkboth{\contentsname}{\contentsname}
  }%
  \@starttoc{toc}%
  \if@restonecol\twocolumn\fi
}

% Index
\renewenvironment{theindex}{%
  \if@twocolumn
    \@restonecolfalse
  \else
    \@restonecoltrue
  \fi
  \twocolumn[\@makeschapterhead{\indexname}]%
  \@mkboth{\indexname}{\indexname}%
  \thispagestyle{plain}%
  \parindent\z@
  \parskip\z@ \@plus .3\p@\relax
  \columnseprule \z@
  \columnsep 35\p@
  \let\item\@idxitem
}{%
  \if@restonecol
    \onecolumn
  \else
    \clearpage
  \fi
}



