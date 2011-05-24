%
% Book design for Git in the Trenches
%

\NeedsTeXFormat{LaTeX2e}[1994/06/01]

\ProvidesClass{gitt}[2011/05/15 v1.0.0 GITT book design]

\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{memoir}%
}
\ProcessOptions*\relax


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

% Set the default formatting options for the Verbatim environment
\fvset{frame=leftline,framerule=1mm,fontsize=\relsize{-3}}

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


