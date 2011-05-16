%
% Book design for Git in the Trenches
%

\NeedsTeXFormat{LaTeX2e}[1994/06/01]

\ProvidesClass{gitt}[2011/05/15 v1.0.0 GITT book design]



\LoadClass[a5paper,openright,12pt]{memoir}

% set paper size
\setlrmarginsandblock{2.16cm}{1.91cm}{*}
\setulmarginsandblock{1.91cm}{1.91cm}{*}
\checkandfixthelayout

% Import packages
\RequirePackage{graphicx}
\RequirePackage{color,fancyvrb,relsize}
\RequirePackage[final]{microtype}
\RequirePackage{tikz}

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

% attempted the same for codeoutput but didn't work
\newenvironment{codeoutput}{\begin{Verbatim}[frame=leftline,framerule=1mm,fontsize=\relsize{-3}]}{\end{Verbatim}}

