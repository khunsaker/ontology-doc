\newpage

# Data Model Structure Diagrams

This section provides visual representations of the Shark2 Knowledge Base data model structure.

## Overview

The following diagram shows the high-level structure of the data model, from the Hub level through Categories, Kinds, and Families for all domains.

\vspace{1cm}

\begin{center}
\makebox[\textwidth][c]{\includegraphics[width=1.2\textwidth]{diagrams/overview.pdf}}
\end{center}

\newpage

## Air Domain Hierarchy

The Aircraft domain follows a detailed classification hierarchy from AirType down to AirInstance. Any level in the chain (AirType through AirSubModel) can be the direct parent of an AirInstance node via the Instance relationship.

\begin{center}
\includegraphics[width=0.9\textwidth]{diagrams/air_domain.pdf}
\end{center}

\newpage

## Ship Domain Hierarchy

The Ship domain hierarchy allows ShipClass nodes to have either ShipType or ShipSubType as parents (via the Class relationship). Similarly, ShipInstance nodes can have either ShipClass or ShipSubClass as parents (via the Instance relationship).

\begin{center}
\includegraphics[width=0.7\textwidth]{diagrams/ship_domain.pdf}
\end{center}

## Future Domain Hierarchies

Additional domain-specific hierarchies for Weapons, Organizations, and Places are currently in development (as well as additional Domains such as Space, Electronics and Terrestrial). These will follow similar patterns to the Air and Ship domains, providing detailed classification structures tailored to each domain's unique characteristics.

\newpage
