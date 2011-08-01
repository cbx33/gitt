%
% Book design for Git in the Trenches
%

\NeedsTeXFormat{LaTeX2e}[1994/06/01]

\ProvidesClass{gitt}[2011/05/15 v1.0.0 GITT book design]

\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{memoir}%
}
\ProcessOptions*\relax


\LoadClass[openright,12pt]{memoir}

% set paper size
\setstocksize{24.59cm}{18.90cm}
%\settrims{1.91cm}{0cm}
\settrimmedsize{\stockheight}{\stockwidth}{*}
\setlrmarginsandblock{2.79cm}{2.29cm}{*}
\setulmarginsandblock{2.91cm}{2.91cm}{*}
%\setmarginnotes{0.5cm}{2cm}{0.2cm}
\checkandfixthelayout

% Reset the figure numbering at the beginning of each chapter and print only
% the figure number (not including the chapter number).
\renewcommand{\thefigure}{\arabic{figure}}

% Import packages
\RequirePackage{pdfpages}
\RequirePackage{graphicx}
\RequirePackage{color,fancyvrb,relsize}
\RequirePackage[final]{microtype}
\RequirePackage{tikz}
\RequirePackage{makeidx}
\RequirePackage{eso-pic}
\PassOptionsToPackage{usenames,dvipsnames,svgnames}{xcolor}
\makeindex

% Import a new font and use the sans-serif version by default
\RequirePackage{lmodern}
\renewcommand{\familydefault}{\sfdefault}

% Put chapters and sections in the toc, only number the chapter
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{0}

% Make chapter names disappear
\renewcommand{\chaptername}{}
\renewcommand{\thechapter}{}
\renewcommand{\tablename}{}
\renewcommand{\thetable}{}

% Print just the chapter name without 'Chapter #.' in the running heads
\renewcommand\chaptermark[1]{\markboth{\memUChead{#1}}{}}%

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
  pagecolor=black,
  plainpages=false,
  pdfpagelabels,
  pdftitle={Git In the Trenches},
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

% Inserts a full-page graphic.
\newcommand{\coverpage}[1]{%
  \thispagestyle{empty}%
  \IfFileExists{#1}{%
    \AddToShipoutPicture*{\put(0,0){\includegraphics[width=\paperwidth,height=\paperheight]{#1}}}%
  }{%
    \ClassWarningNoLine{gitt}{Missing cover page graphic:\MessageBreak #1}%
  }%
  \null\cleardoublepage%
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
    %morecomment=[l][\tiny\bfseries\ttfamily]{john@satsuki:},
    %morecomment=[l][\tiny\bfseries\ttfamily]{rob@mimi:}
    %moredelim=[is][\tiny\bfseries\ttfamily]{|||}{|||}
  }
}{}
